# Generated by Django 4.1.2 on 2022-10-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_alter_police_police_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='police_designation',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='কর্মরত পদ'),
        ),
        migrations.AlterField(
            model_name='police',
            name='police_political_background',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='রাজনৈতিক ইতিহাস'),
        ),
    ]