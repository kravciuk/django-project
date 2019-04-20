# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps import views as sitemap_views
from django.views.generic import TemplateView
from django.contrib import admin

from sitetree.sitetreeapp import register_i18n_trees

from .sitemaps import ProjectSitemap
from . import views

# handler404 = 'project.views.error404'

register_i18n_trees(['header_menu'])

sitemaps = {
    'general': ProjectSitemap(),
}

urlpatterns = [
    url(r'^su/', admin.site.urls),

    url(r'^sitemap\.xml$', sitemap_views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap_views.sitemap, {'sitemaps': sitemaps}),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^select2/', include('django_select2.urls')),

]

urlpatterns += i18n_patterns(
    url(r'^$',TemplateView.as_view(template_name='index.html'), name="homepage"),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^share/', include('vcms.share.urls')),
    url(r'^', include('vcms.content.urls')),

    prefix_default_language=False
)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
