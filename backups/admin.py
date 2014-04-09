from django.contrib import admin

# Register your models here.
from backups.models import Database, DBDump

admin.site.register(Database)
admin.site.register(DBDump)