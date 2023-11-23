# Generated by Django 4.1.5 on 2023-02-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menufoods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
