# Generated by Django 3.2.4 on 2021-07-19 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0010_auto_20210719_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationrating',
            name='user',
        ),
        migrations.AddField(
            model_name='applicationrating',
            name='user_profile',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='jury.userprofile'),
        ),
    ]
