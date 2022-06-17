# Generated by Django 3.2.6 on 2021-08-29 11:46

from django.db import migrations


def create_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    LogEntry = apps.get_model('admin', 'LogEntry')

    ct = ContentType.objects.get_for_model(LogEntry)
    opts = LogEntry._meta
    codename = '{}_{}'.format('archive', opts.object_name.lower())
    params = dict(codename=codename,
                  content_type=ct,
                  defaults={'name': 'Can archive logs'})
    Permission.objects.get_or_create(**params)


def remove_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    LogEntry = apps.get_model('admin', 'LogEntry')

    ct = ContentType.objects.get_for_model(LogEntry)
    opts = LogEntry._meta
    codename = '{}_{}'.format('archive', opts.object_name.lower())
    params = dict(codename=codename,
                  content_type=ct)
    Permission.objects.filter(**params).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_permission, remove_permission)
    ]
