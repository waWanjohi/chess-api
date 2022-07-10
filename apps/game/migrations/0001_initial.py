# Generated by Django 4.0.6 on 2022-07-10 13:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=300, primary_key=True, serialize=False)),
                ('captured_piece', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=300, primary_key=True, serialize=False)),
                ('from_pos', models.CharField(max_length=10)),
                ('to_pos', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.CharField(default=uuid.uuid4, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('captures', models.ManyToManyField(to='game.capture')),
                ('moves', models.ManyToManyField(to='game.move')),
            ],
        ),
    ]
