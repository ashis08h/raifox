# Generated by Django 3.0.3 on 2020-07-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('course_start_date', models.DateTimeField()),
                ('course_end_date', models.DateTimeField()),
            ],
        ),
    ]
