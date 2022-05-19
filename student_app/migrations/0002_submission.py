# Generated by Django 4.0.4 on 2022-05-18 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_homework'),
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('statement', models.CharField(max_length=1000)),
                ('grade', models.FloatField(blank=True, default=None, null=True)),
                ('homework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses_app.homework')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_app.student')),
            ],
        ),
    ]