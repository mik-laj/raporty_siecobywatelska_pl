from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from raporty_siecobywatelska_pl.ranking.views import RankingList

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^$', RankingList.as_view(), name="home"),

    # Admin
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('raporty_siecobywatelska_pl.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^', include('raporty_siecobywatelska_pl.ranking.urls', namespace='rankings')),
    url(r'^', include('raporty_siecobywatelska_pl.institutions.urls', namespace='institutions')),
    url(r'^', include('raporty_siecobywatelska_pl.answers.urls', namespace='answers')),
    url(r'^', include('raporty_siecobywatelska_pl.questionnaire.urls', namespace='questionnaire')),
    url(r'^', include('raporty_siecobywatelska_pl.articles.urls', namespace='articles')),
    url(r'^', include('raporty_siecobywatelska_pl.analysis.urls', namespace='analysis')),
    url(r'^teryt/', include('raporty_siecobywatelska_pl.teryt.urls', namespace='teryt')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
