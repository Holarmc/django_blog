# Generated by Django 3.0.5 on 2020-06-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200608_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publication_date',
            new_name='pub_date',
        ),
    ]
