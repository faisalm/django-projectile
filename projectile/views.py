from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from projectile.models import Project
from simplepages.models import SimplePageCategory

def index(request, template_name='front/index.html'):
    listed_featured = 8
    listed_thumbs = 6
    try:
        qs_featured_projects = Project.objects.filter(is_featured=True, is_inactive=False, is_deleted=False).order_by('-priority')
        if len(qs_featured_projects) > listed_featured:
            qs_featured_projects = qs_featured_projects[:listed_featured]
    except Project.DoesNotExist:
        qs_featured_projects = []
    try:
        qs_thumb_projects = Project.objects.filter(is_thumb=True, is_inactive=False, is_deleted=False).order_by('?')
        if len(qs_thumb_projects) > listed_thumbs:
            qs_thumb_projects = qs_thumb_projects[:listed_thumbs]
    except Project.DoesNotExist:
        qs_thumb_projects = []
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def projects(request, template_name='front/projects.html'):
    try:
        qs_thumb_projects = Project.objects.filter(is_thumb=True, is_inactive=False, is_deleted=False).order_by('-created_at')
    except Project.DoesNotExist:
        qs_thumb_projects = []
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def project_detail(request, project_slug, template_name='front/project_detail.html'):
    project = get_object_or_404(Project, slug=project_slug)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))