# Generated by Django 4.1.4 on 2022-12-10 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0008_defaultuser_group_remove_companybid_students_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='id_student',
            new_name='identification_student',
        ),
    ]
