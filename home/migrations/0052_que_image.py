# Generated by Django 4.1.3 on 2023-02-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_subject_total_marks_subject_total_que'),
    ]

    operations = [
        migrations.AddField(
            model_name='que',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='que/images'),
        ),
    ]