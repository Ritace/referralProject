# Generated by Django 3.0.2 on 2020-01-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
