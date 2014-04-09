from django.contrib.auth.hashers import make_password
from django.db import models


class Database(models.Model):
    alias = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    host = models.CharField(max_length=256)
    user = models.CharField(max_length=256)
    password = models.CharField(max_length=128)
    port = models.PositiveIntegerField()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)


class DBDump(models.Model):
    METHOD_CHOICES = (('SCHEDULED', 1), ('MANUAL', 2))

    database = models.ForeignKey(Database)
    method = models.CharField(max_length=64)
    dump_date = models.DateTimeField(auto_created=True)
    dump_file = models.CharField(max_length=1024)
    time_to_dump = models.TimeField()
    size = models.PositiveIntegerField()


