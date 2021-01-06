from datetime import date

from django.test import TestCase

from clients.models import Client

from freezegun import freeze_time


@freeze_time("2020-01-01")
class TestClient(TestCase):

    def test_age(self):
        c = Client.objects.create(birth_date=date(2010, 1, 1))
        self.assertEqual(c.age(), 10)
