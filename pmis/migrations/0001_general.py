# Generated by Django 4.2.7 on 2023-11-23 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, max_length=100)),
                ('name_bangla', models.CharField(blank=True, max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('freedom_fighter', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('lpr_prl_date', models.DateField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('cadre_date', models.DateField(blank=True, null=True)),
                ('confirmation_g_o_date', models.DateField(blank=True, null=True)),
                ('govt_id', models.CharField(blank=True, max_length=100)),
                ('rank', models.CharField(blank=True, max_length=100)),
                ('home_district', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('organisation', models.CharField(blank=True, max_length=100)),
                ('cadre', models.CharField(blank=True, max_length=100)),
                ('batch', models.CharField(blank=True, max_length=100)),
                ('religion', models.CharField(blank=True, max_length=100)),
                ('marital_stat', models.CharField(blank=True, max_length=100)),
                ('nid', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255)),
                ('purpose', models.CharField(blank=True, max_length=100)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_type', models.CharField(choices=[('LM', 'LOCAL (MANDATORY)'), ('L', 'LOCAL'), ('F', 'FOREIGN')], max_length=50)),
                ('course_title', models.CharField(blank=True, max_length=255)),
                ('institution', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spouse_name', models.CharField(blank=True, max_length=100)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('home_district', models.CharField(blank=True, max_length=100)),
                ('organisation', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spouse', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadre', models.CharField(blank=True, max_length=100)),
                ('govt_service_date', models.DateField(blank=True, null=True)),
                ('gazetted_date', models.DateField(blank=True, null=True)),
                ('encadrement_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=255)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(blank=True, max_length=255)),
                ('periodical_monograph', models.CharField(blank=True, max_length=255)),
                ('journals', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Prosecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_of_offence', models.CharField(blank=True, max_length=100)),
                ('punishment', models.CharField(blank=True, max_length=100)),
                ('remarks', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prosecution', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(blank=True, max_length=100)),
                ('nature_of_promotion', models.CharField(blank=True, max_length=100)),
                ('pay_scale', models.CharField(blank=True, max_length=100)),
                ('promotion_date', models.DateField(blank=True, null=True)),
                ('g_o_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_or_house_or_road', models.CharField(blank=True, max_length=100)),
                ('post_office', models.CharField(blank=True, max_length=100)),
                ('police_station', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('telephone_no', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='present', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('organisation', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('pay_scale', models.CharField(blank=True, max_length=100)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Permanent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_or_house_or_road', models.CharField(blank=True, max_length=100)),
                ('post_office', models.CharField(blank=True, max_length=100)),
                ('police_station', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('telephone_no', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permanent', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_employeer', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('type_of_service', models.CharField(blank=True, max_length=255)),
                ('posting', models.CharField(blank=True, max_length=255)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(blank=True, max_length=10)),
                ('read', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('write', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('speak', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Honour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_award', models.CharField(blank=True, max_length=255)),
                ('ground', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='honour', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_institution', models.CharField(blank=True, max_length=255)),
                ('principal_subject', models.CharField(blank=True, max_length=100)),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('passing_year', models.CharField(blank=True, max_length=100)),
                ('result', models.CharField(blank=True, max_length=100)),
                ('gpa_or_cgpa', models.CharField(blank=True, max_length=100)),
                ('distinction', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='pmis.person')),
            ],
        ),
        migrations.CreateModel(
            name='Abroad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(blank=True, max_length=255)),
                ('organisation', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='abroad', to='pmis.person')),
            ],
        ),
    ]