# Generated by Django 2.2.7 on 2019-12-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipefinderApp', '0006_auto_20191204_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooktime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cook_times', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='cooking_time',
        ),
        migrations.AddField(
            model_name='preferences',
            name='cooking_time',
            field=models.ManyToManyField(to='recipefinderApp.Cooktime'),
        ),
    ]