# Generated by Django 4.1.5 on 2023-02-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='fav',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
