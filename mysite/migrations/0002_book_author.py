# Generated by Django 4.0.2 on 2022-03-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(default=1, max_length=33),
            preserve_default=False,
        ),
    ]
