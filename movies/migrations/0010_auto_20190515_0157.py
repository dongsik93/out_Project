# Generated by Django 2.1.5 on 2019-05-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_moviedetail_score_reples'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='audiAcc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='movieCd',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rank',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
