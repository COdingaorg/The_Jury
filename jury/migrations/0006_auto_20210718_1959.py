# Generated by Django 3.2.4 on 2021-07-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0005_auto_20210718_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_account',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram_account',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_account',
            field=models.CharField(max_length=50),
        ),
    ]
