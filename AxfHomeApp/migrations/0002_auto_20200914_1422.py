# Generated by Django 2.2.14 on 2020-09-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AxfHomeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.AlterModelTable(
            name='axfwheel',
            table='axf_wheel',
        ),
    ]
