# Generated by Django 5.0.6 on 2024-06-26 08:58

import django_tenants.postgresql_backend.base
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dc_tenant_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='schema_name',
            field=models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name]),
        ),
    ]
