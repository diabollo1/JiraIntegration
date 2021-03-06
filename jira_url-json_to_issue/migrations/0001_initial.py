# Generated by Django 3.1.3 on 2020-11-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_insert', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=20)),
                ('json', models.CharField(max_length=200)),
                ('issue_date_adding', models.DateTimeField()),
                ('issue_id', models.CharField(max_length=200)),
                ('issue_key', models.CharField(max_length=200)),
                ('issue_url', models.CharField(max_length=200)),
            ],
        ),
    ]
