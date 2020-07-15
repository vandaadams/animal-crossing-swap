# Generated by Django 3.0.7 on 2020-07-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0007_auto_20200714_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZingChartConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('xAxis', models.CharField(max_length=20)),
                ('yAxis', models.CharField(max_length=20)),
                ('theme', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'zingchart_config',
            },
        ),
        migrations.CreateModel(
            name='ZingChartSeriesData1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'zingchart_data_1',
            },
        ),
    ]
