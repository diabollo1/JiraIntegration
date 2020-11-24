from datetime import datetime

from django.test import TestCase
from .models import Issue, json_to_send


class QueueTestCase(TestCase):

    def test_add_issue_to_database(self):
        i = Issue(date_insert=datetime.now(), source="django", json="{abc}")
        self.assertEqual(json_to_send(), True)

    def test_add_issue_to_database(self):
        i = Issue(date_insert=datetime.now(), source="django", json="{abc}")
        self.assertEqual(json_to_send(), True)
