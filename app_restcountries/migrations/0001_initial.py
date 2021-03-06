# Generated by Django 3.2.5 on 2021-08-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=200)),
                ('alphacode2', models.CharField(default='N/A', max_length=200)),
                ('capital', models.CharField(default='N/A', max_length=200)),
                ('population', models.IntegerField(default=0)),
                ('timezone', models.TextField(default='N/A')),
                ('flag', models.TextField(default='N/A')),
                ('languages', models.TextField(default='N/A')),
                ('neighbours', models.TextField(default='N/A')),
            ],
        ),
    ]
