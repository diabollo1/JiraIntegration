# Generated by Django 3.1.3 on 2020-11-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira_url-json_to_issue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_date_adding',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]