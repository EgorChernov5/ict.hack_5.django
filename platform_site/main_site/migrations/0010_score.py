# Generated by Django 4.1.4 on 2022-12-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0009_rename_id_student_rate_identification_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_score', models.FloatField()),
            ],
        ),
    ]