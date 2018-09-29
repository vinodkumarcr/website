# Generated by Django 2.0.2 on 2018-09-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images')),
                ('summary', models.TextField(max_length=500)),
            ],
        ),
    ]
