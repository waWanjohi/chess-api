# Generated by Django 4.0.6 on 2022-07-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='color',
            field=models.CharField(default='fuck', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='move',
            name='color',
            field=models.CharField(default='fuck', max_length=10),
            preserve_default=False,
        ),
    ]
