from django.conf.urls import patterns, url
from backups.views import BackupHome, DatabaseListView

__author__ = 'jbean'
urlpatterns = patterns(
    'backups.views',
    url(r'^$', BackupHome.as_view(), name='home'),
    url(r'^database_list/', DatabaseListView.as_view(), name='db_list')
)
