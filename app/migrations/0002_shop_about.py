# Generated by Django 4.0.3 on 2022-03-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
