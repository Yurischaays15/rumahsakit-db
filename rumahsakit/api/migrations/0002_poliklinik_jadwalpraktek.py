# Generated by Django 4.0.2 on 2022-02-28 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poliklinik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('kode', models.TextField()),
                ('icon', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JadwalPraktek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.TextField()),
                ('schedule', models.TextField()),
                ('poliklinik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.poliklinik')),
            ],
        ),
    ]
