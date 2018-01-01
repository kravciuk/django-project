# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps import views as sitemap_views
from django.contrib import admin

from .sitemaps import ProjectSitemap
from . import views

handler404 = 'project.views.error404'

sitemaps = {
    'general': ProjectSitemap(),
}

urlpatterns = [
    url(r'^su/', admin.site.urls),

    # url(r'example/', include('apps.example.urls')),
    url(r'^$', views.index_page, name="index_page"),

    url(r'^sitemap\.xml$', sitemap_views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap_views.sitemap, {'sitemaps': sitemaps}),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^select2/', include('django_select2.urls')),

    url(r'^share/', include('vcms.share.urls')),
    url(r'^content/', include('vcms.content.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
