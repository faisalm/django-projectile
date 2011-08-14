from django.conf.urls.defaults import patterns

urlpatterns = patterns('projectile.views',
    (r'^project/$', 'projects', {'template_name': 'front/projects.html'}, 'projects'),
    (r'^project/(?P<project_slug>[-\w]+)/$', 'project_detail', {'template_name': 'front/project-detail.html'}, 'project_detail'),
)
