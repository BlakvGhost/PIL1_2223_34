# Generated by Django 4.2.2 on 2023-06-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_subject_bgcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='bgColor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
