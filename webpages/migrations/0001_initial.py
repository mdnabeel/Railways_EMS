# Generated by Django 3.2.3 on 2021-05-25 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FaultDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fault_no', models.IntegerField()),
                ('fault_description', models.TextField()),
                ('fault_date', models.DateField()),
                ('rectification_date', models.CharField(blank=True, max_length=20, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('current_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.status')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.department')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.station')),
            ],
        ),
    ]
