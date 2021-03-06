# Generated by Django 3.2.8 on 2021-10-14 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('num_pages', models.IntegerField(default=0, null=True)),
                ('isbn13', models.CharField(blank=True, max_length=13, null=True)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_type',
            field=models.CharField(choices=[('In Person', 'In Person'), ('Zoom', 'Zoom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='student',
            field=models.ManyToManyField(to='institution.Student'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.tutor'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=7, null=True)),
                ('course_name', models.CharField(choices=[('College Algebra', 'College Algebra'), ('Calculus', 'Calculus'), ('Plane Trigonometry', 'Plane Trigonometry'), ('Statistics', 'Statistics'), ('Functions And Modeling', 'Functions And Modeling')], max_length=100, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.book')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.instructor')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='institution.Course'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='course',
            field=models.ManyToManyField(to='institution.Course'),
        ),
    ]
