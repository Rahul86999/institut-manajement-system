# Generated by Django 2.1.7 on 2019-02-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='fees',
            field=models.IntegerField(default=170),
        ),
        migrations.AlterField(
            model_name='payfee',
            name='panding_fee',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
