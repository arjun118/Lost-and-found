# Generated by Django 4.1.2 on 2022-11-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='found',
            field=models.BooleanField(default=False),
        ),
    ]
