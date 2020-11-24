from django.db import models


def json_to_send():
    return True


class Issue(models.Model):
    date_insert = models.DateTimeField(auto_now=False, auto_now_add=True)
    source = models.CharField(max_length=20)
    json = models.CharField(max_length=200)
    issue_date_adding = models.DateTimeField(auto_now=False, auto_now_add=False)
    issue_id = models.CharField(max_length=200)
    issue_key = models.CharField(max_length=200)
    issue_url = models.CharField(max_length=200)

    def __str__(self):
        return self.json

    def issue_to_create(self):
        pass
