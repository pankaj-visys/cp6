# Generated by Django 4.1.3 on 2023-01-14 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0033_ans_score_alter_ans_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.FloatField(default=0)),
                ('wrong_answer', models.FloatField(default=0)),
                ('not_answer', models.FloatField(default=0)),
                ('ppr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ppr')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
