# Generated by Django 3.2.7 on 2021-10-17 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('product', models.CharField(max_length=254)),
                ('UUID', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MicroCenter',
            fields=[
                ('MicroCenter_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MicroCenter_SKU', models.IntegerField(primary_key=True, serialize=False)),
                ('MicroCenter_ModelNumber', models.CharField(max_length=128)),
                ('MicroCenter_URL', models.CharField(max_length=256)),
                ('MicroCenter_UUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='Gamestop',
            fields=[
                ('Gamestop_SKU', models.IntegerField(primary_key=True, serialize=False)),
                ('Gamestop_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Gamestop_URL', models.CharField(max_length=256)),
                ('Gamestop_Status', models.CharField(max_length=32)),
                ('Gamestop_UUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='BH',
            fields=[
                ('BH_SKU', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('BH_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BH_Status', models.CharField(max_length=32)),
                ('BH_URL', models.CharField(max_length=256)),
                ('BH_UUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='BestBuy',
            fields=[
                ('BestBuy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BestBuy_Status', models.CharField(max_length=32)),
                ('BestBuy_Ratings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('BestBuy_Review', models.IntegerField()),
                ('BestBuy_ModelNumber', models.CharField(max_length=128)),
                ('BestBuy_SKU', models.IntegerField(primary_key=True, serialize=False)),
                ('BestBuy_URL', models.CharField(max_length=256)),
                ('BestBuy_UUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='AD',
            fields=[
                ('AD_SKU', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('AD_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('AD_Status', models.CharField(max_length=32)),
                ('AD_URL', models.CharField(max_length=256)),
                ('AD_UUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
    ]
