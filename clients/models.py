from django.contrib.auth.models import User
from django.db.models import Model, CASCADE, OneToOneField, CharField, DateField

from datetime import date

from django_prometheus.models import ExportModelOperationsMixin


class Client(ExportModelOperationsMixin('client'), Model):
    user = OneToOneField(User, on_delete=CASCADE, null=True, blank=True)
    cin_number = CharField(max_length=8, null=True, blank=True)
    function = CharField(max_length=255, null=True, blank=True)
    birth_date = DateField(null=True, blank=True)

    def age(self):
        return date.today().year - self.birth_date.year
