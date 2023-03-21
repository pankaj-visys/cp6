# Generated by Django 4.1.3 on 2023-01-07 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_questions_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ppr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=300, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='Media/Yt_Thumbnail')),
                ('subject', models.CharField(max_length=300, null=True)),
                ('time_duration', models.IntegerField(null=True)),
                ('preview', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
    ]
