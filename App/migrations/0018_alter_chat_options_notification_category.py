# Generated by Django 4.2.2 on 2023-06-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_rename_created_by_chat_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={},
        ),
        migrations.AddField(
            model_name='notification',
            name='category',
            field=models.CharField(default='shedule', max_length=50),
        ),
    ]
