# Generated by Django 3.0.2 on 2020-01-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200113_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='alternative_phone_number1',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='alternative_phone_number2',
        ),
        migrations.AddField(
            model_name='referral',
            name='country_of_residense',
            field=models.CharField(default='India', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referral',
            name='nationality',
            field=models.CharField(default='Indian', max_length=50),
            preserve_default=False,
        ),
    ]
