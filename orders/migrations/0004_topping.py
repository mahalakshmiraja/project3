# Generated by Django 2.0.7 on 2018-07-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_item_displayname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppingName', models.CharField(max_length=64)),
                ('toppingPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]