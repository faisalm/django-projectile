from django.conf.urls.defaults import patterns

urlpatterns = patterns('projectile.views',
    (r'^$', 'index', {'template_name': 'front/index.html'}, 'home'),
    (r'^projekt/$', 'projects', {'template_name': 'front/projects.html'}, 'projects'),
    (r'^projekt/(?P<project_slug>[-\w]+)/$', 'project_detail', {'template_name': 'front/project-detail.html'}, 'project_detail'),
    # regex, view path, {dict}, name
)