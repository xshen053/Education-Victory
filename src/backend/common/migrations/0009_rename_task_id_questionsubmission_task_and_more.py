# Generated by Django 4.1.4 on 2023-09-01 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_questionsubmission_content_alter_task_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionsubmission',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='user',
        ),
    ]
