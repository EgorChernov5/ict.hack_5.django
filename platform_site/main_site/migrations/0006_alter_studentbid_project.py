# Generated by Django 4.1.4 on 2022-12-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0005_alter_companyprojects_checking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbid',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MainSite.studentprojects', verbose_name='Student project'),
        ),
    ]