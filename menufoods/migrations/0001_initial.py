# Generated by Django 4.1.5 on 2023-02-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=5000)),
                ('price', models.IntegerField(verbose_name=10)),
                ('is_premium', models.BooleanField(null=True)),
            ],
        ),
    ]
