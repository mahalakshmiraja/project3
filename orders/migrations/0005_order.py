# Generated by Django 2.0.7 on 2018-07-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderItem', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
