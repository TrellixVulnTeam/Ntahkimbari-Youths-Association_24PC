# Generated by Django 2.0.6 on 2018-07-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0009_auto_20180630_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='community_work',
            name='tools',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]
