# Generated by Django 2.1.5 on 2019-05-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_moviedetail_dialog'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='image_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
