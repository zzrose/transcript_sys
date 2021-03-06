# Generated by Django 2.0.3 on 2018-11-10 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='Grade')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Grade Info',
                'verbose_name_plural': 'Grade Info',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transcript.Degree', verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student'),
        ),
    ]
