# Generated by Django 2.1.2 on 2018-10-26 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20181026_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='board',
            new_name='bo',
        ),
    ]