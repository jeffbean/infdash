from django.views.generic import TemplateView, ListView

from backups.models import Database


class BackupHome(TemplateView):
    template_name = 'backups/backups_home.html'


class DatabaseListView(ListView):
    model = Database