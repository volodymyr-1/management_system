# Generated by Django 3.1.7 on 2021-03-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20210311_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventtype'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]