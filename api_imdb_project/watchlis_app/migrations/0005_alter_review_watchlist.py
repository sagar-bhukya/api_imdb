# Generated by Django 5.0.7 on 2024-07-30 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlis_app', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='watchList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='watchlis_app.watchlist'),
        ),
    ]
