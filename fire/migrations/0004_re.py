# Generated by Django 3.0 on 2020-07-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0003_auto_20200714_0532'),
    ]

    operations = [
        migrations.CreateModel(
            name='re',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
