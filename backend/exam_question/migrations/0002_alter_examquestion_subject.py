# Generated by Django 5.1 on 2024-08-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examquestion',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
