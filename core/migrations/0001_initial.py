# Generated by Django 3.0.5 on 2020-11-13 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('pages', models.IntegerField()),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
