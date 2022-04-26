# Generated by Django 4.0.3 on 2022-04-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_shop_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senduser', models.CharField(max_length=50)),
                ('aduser', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]