# Generated by Django 4.1.3 on 2023-02-07 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_subject_title_alter_subject_slug_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='ans',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
    ]
