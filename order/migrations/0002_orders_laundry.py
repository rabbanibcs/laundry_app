# Generated by Django 3.2.5 on 2021-07-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='laundry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='laundry.laundry'),
            preserve_default=False,
        ),
    ]
