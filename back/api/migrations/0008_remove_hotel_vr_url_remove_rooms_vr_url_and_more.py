# Generated by Django 4.2.6 on 2023-10-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_orders"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hotel",
            name="vr_url",
        ),
        migrations.RemoveField(
            model_name="rooms",
            name="vr_url",
        ),
        migrations.AlterField(
            model_name="hotel",
            name="address",
            field=models.CharField(max_length=255, null=True, verbose_name="Salgysy"),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="name",
            field=models.CharField(max_length=255, null=True, verbose_name="Ady"),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="web_url",
            field=models.CharField(max_length=255, null=True, verbose_name="Salgysy"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="address",
            field=models.CharField(max_length=255, null=True, verbose_name="Salgysy"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="bar",
            field=models.BooleanField(default=True, verbose_name="Kafe"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="bath",
            field=models.BooleanField(default=True, verbose_name="Duş"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="car",
            field=models.BooleanField(default=True, verbose_name="Awto park"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="description",
            field=models.TextField(null=True, verbose_name="Maglumaty"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="hotel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="api.hotel",
                verbose_name="Myhmanhana",
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="img",
            field=models.ImageField(
                null=True, upload_to="room_images", verbose_name="Suraty"
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="name",
            field=models.CharField(max_length=255, null=True, verbose_name="Ady"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="person_place",
            field=models.CharField(max_length=50, null=True, verbose_name="Ýer sany"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="price",
            field=models.CharField(max_length=255, null=True, verbose_name="Bahasy"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="sport",
            field=models.BooleanField(default=True, verbose_name="Fitness zal"),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="wifi",
            field=models.BooleanField(default=True, verbose_name="Wifi"),
        ),
    ]
