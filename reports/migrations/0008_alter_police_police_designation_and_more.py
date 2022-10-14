# Generated by Django 4.1.2 on 2022-10-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_remove_police_police_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='police_designation',
            field=models.CharField(blank=True, default='প্রযোজ্য নহে', max_length=200, verbose_name='কর্মরত পদ'),
        ),
        migrations.AlterField(
            model_name='police',
            name='police_political_background',
            field=models.CharField(blank=True, default='প্রযোজ্য নহে', max_length=2000, verbose_name='রাজনৈতিক ইতিহাস'),
        ),
    ]
