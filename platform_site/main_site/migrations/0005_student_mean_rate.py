# Generated by Django 4.1.4 on 2022-12-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0004_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mean_rate',
            field=models.FloatField(default=0, verbose_name='Mean rate'),
        ),
    ]
