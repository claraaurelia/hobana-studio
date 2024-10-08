# Generated by Django 5.1.1 on 2024-09-17 09:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
