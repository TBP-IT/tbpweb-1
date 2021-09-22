# Generated by Django 2.2.8 on 2021-09-22 22:27

import course_files.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_ext', models.CharField(max_length=5)),
                ('verified', models.BooleanField(blank=True, default=False)),
                ('flags', models.PositiveSmallIntegerField(default=0)),
                ('blacklisted', models.BooleanField(default=False)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('exam_number', models.CharField(choices=[('un', 'Unknown'), ('mt1', 'Midterm 1'), ('mt2', 'Midterm 2'), ('mt3', 'Midterm 3'), ('mt4', 'Midterm 4'), ('final', 'Final')], max_length=5)),
                ('exam_type', models.CharField(choices=[('exam', 'Exam'), ('soln', 'Solution')], max_length=4)),
                ('exam_file', models.FileField(upload_to=course_files.models.generate_courseitem_filepath)),
                ('course_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInstance')),
                ('submitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_all_exams', 'Can view blacklisted and flagged exams'),),
            },
        ),
        migrations.CreateModel(
            name='InstructorPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_allowed', models.BooleanField(help_text='Has this instructor given permission to post files?')),
                ('correspondence', models.TextField(blank=True, help_text='Reason for why permission was or was not given.')),
                ('instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Instructor')),
            ],
            options={
                'ordering': ('instructor',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(help_text='Why is this item being flagged?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('resolution', models.TextField(blank=True)),
                ('resolved', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(help_text='The exam that has an issue.', on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
