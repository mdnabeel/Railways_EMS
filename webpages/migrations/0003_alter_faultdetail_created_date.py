# Generated by Django 3.2.3 on 2021-05-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_alter_faultdetail_fault_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faultdetail',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
