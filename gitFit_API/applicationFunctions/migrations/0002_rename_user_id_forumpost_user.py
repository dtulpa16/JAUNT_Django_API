# Generated by Django 3.2.8 on 2021-10-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationFunctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='user_id',
            new_name='user',
        ),
    ]