# Generated by Django 4.1.4 on 2023-01-22 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_courses_complete_hours_updated_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableUpdatedCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.updated_courses',),
        ),
    ]
