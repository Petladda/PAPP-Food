# Generated by Django 4.1.5 on 2023-02-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menufoods', '0003_remove_food_title_food_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='food',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
