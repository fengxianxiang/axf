# Generated by Django 2.2.14 on 2020-09-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AxfHomeApp', '0002_auto_20200914_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
    ]
