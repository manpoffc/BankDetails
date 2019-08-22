# Generated by Django 2.2.4 on 2019-08-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankings_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ifsc', models.CharField(max_length=50)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=60)),
            ],
        ),
    ]