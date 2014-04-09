from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


class DashHome(TemplateView):
    template_name = 'home.html'


urlpatterns = patterns(
    '',
    url(r'^$', DashHome.as_view(), name='home'),
    url(r'^backups/', include('backups.urls'), name='backups'),
    url(r'^admin/', include(admin.site.urls)),
)
