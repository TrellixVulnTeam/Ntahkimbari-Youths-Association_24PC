# Generated by Django 2.0.6 on 2018-06-28 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0002_auto_20180627_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
