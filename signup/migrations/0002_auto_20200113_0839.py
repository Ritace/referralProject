# Generated by Django 3.0.2 on 2020-01-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ACN_of_previous_yatra_attended',
            field=models.CharField(default='123123', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country_of_residense',
            field=models.CharField(default='Indian', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default='1994-06-30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(default='Indian', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year_of_previous_yatra_attended',
            field=models.DateField(default='2015-06-30'),
            preserve_default=False,
        ),
    ]
