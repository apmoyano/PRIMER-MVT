# Generated by Django 4.0.3 on 2022-03-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fliamoyano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('parentesco', models.CharField(max_length=15)),
                ('estado_civil', models.CharField(max_length=15)),
            ],
        ),
    ]
