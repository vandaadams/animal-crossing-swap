# Generated by Django 3.0.7 on 2020-07-14 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackerapp', '0002_auto_20200712_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnip',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turnip',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday')], default='Monday', max_length=10),
        ),
        migrations.AlterField(
            model_name='turnip',
            name='time',
            field=models.CharField(choices=[('M', 'Morning'), ('E', 'Evening')], default='Morning', max_length=10),
        ),
    ]
