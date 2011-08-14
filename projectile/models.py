from django.db import models

# Create your models here.
class ProjectCategory(models.Model):
    # Web, mobile, print etc
    title = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
        ordering = ['title']
    
    def __unicode__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(ProjectCategory)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, help_text='Used as seo friendly url.')
    override_url = models.CharField(max_length=100, blank=True, verbose_name='Override URL', help_text='Only used if not blank.')
    meta_keywords = models.CharField(max_length=100, blank=True, verbose_name='Meta Keywords', help_text="For SEO purposes.")
    meta_description = models.CharField(max_length=100, blank=True, verbose_name='Meta Description', help_text="For SEO purposes.")
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    client = models.CharField(max_length=100, help_text='Name of end-client/end-user.')
    agency = models.CharField(max_length=100, blank=True, help_text='Name of agency, if any.')
    role = models.CharField(max_length=100, blank=True, help_text='Roles played in this project. Separate with comma.')
    tech = models.CharField(max_length=100, blank=True, verbose_name='Technology', help_text='Technologies used in this project. Separate with comma.')
    tools = models.CharField(max_length=100, blank=True, help_text='Tools used in this project. Separate with comma.')
    link = models.URLField(blank=True, help_text='Link to the live/archived project on the web.')
    priority = models.IntegerField(default=0, help_text='The highest number comes first.')
    is_featured = models.BooleanField(verbose_name='Featured', help_text='Show project among featured.')
    is_thumb = models.BooleanField(verbose_name='Thumbnail', help_text='Show project in thumbnail list.')
    is_inactive = models.BooleanField(verbose_name='Inactive', help_text='Hide project from all views.')
    is_deleted = models.BooleanField(editable=False, help_text='Only visible to arch.')
    created_at = models.DateTimeField()
    
    class Meta:
        ordering = ['-priority']

    def __unicode__(self):
        return self.title
    
    # Functions related to images
    def get_featured_image(self):
        try:
            return ProjectImage.objects.filter(project=self.id, category=ProjectImage.FEATURED_CATEGORY).latest('created_at')
        except ProjectImage.DoesNotExist:
            # Returns none if there arent any featured images
            # Use an if-statement in the template to check if none and then exclude it from the selection
            return None

    def get_thumb_image(self):
        try:
            return ProjectImage.objects.filter(project=self.id, category=ProjectImage.THUMBNAIL_CATEGORY).latest('created_at')
        except ProjectImage.DoesNotExist:
            # Returns none if there arent any featured images
            # Use an if-statement in the template to check if none and then exclude it from the selection
            return None

    def get_detail_images(self):
        try:
            # Returns a queryset of images related to this instance
            # Sorts by priority
            return ProjectImage.objects.filter(project=self.id, category=ProjectImage.DETAIL_CATEGORY).order_by('-priority')
        except ProjectImage.DoesNotExist:
            # Returns an empty queryset/list
            return []

    def get_project_year(self):
        return "%s" % self.created_at.strftime('%Y')
    
    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', (), {'project_slug': self.slug})

class ProjectImage(models.Model):
    STANDARD_CATEGORY = 1
    FEATURED_CATEGORY = 2
    THUMBNAIL_CATEGORY = 3
    DETAIL_CATEGORY = 4
    CATEGORY_CHOICES = (
        (STANDARD_CATEGORY, 'Standard'),
        (FEATURED_CATEGORY, 'Featured'),
        (THUMBNAIL_CATEGORY, 'Thumbnail'),
        (DETAIL_CATEGORY, 'Detail'),
    )
    project = models.ForeignKey(Project)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=STANDARD_CATEGORY)
    path = models.ImageField(upload_to='images/projects')
    priority = models.IntegerField(default=0, help_text='Highest number first.')
    title = models.CharField(max_length=100, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    class Meta:
        verbose_name = 'Project Image'
    
    def __unicode__(self):
        return "%s - %s" % (self.project.title, self.title)
