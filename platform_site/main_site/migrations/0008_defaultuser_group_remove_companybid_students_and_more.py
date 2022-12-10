# Generated by Django 4.1.4 on 2022-12-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0007_studentbid_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultuser',
            name='group',
            field=models.CharField(choices=[('S', 'Student'), ('C', 'Company')], default=1, max_length=1, verbose_name='Group'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='companybid',
            name='students',
        ),
        migrations.AddField(
            model_name='companybid',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='MainSite.student', verbose_name='Students'),
        ),
    ]