# Generated by Django 4.2.3 on 2023-07-10 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0008_farmer_delete_farmerdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='taken_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_by', to='authentication.farmer')),
                ('taken_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_from', to='authentication.farmer')),
            ],
            options={
                'verbose_name_plural': 'Taken Equipment',
            },
        ),
        migrations.CreateModel(
            name='shared_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=100)),
                ('equipment_company', models.CharField(blank=True, max_length=100)),
                ('equipment_model', models.CharField(blank=True, max_length=100)),
                ('equipment_id', models.CharField(max_length=100)),
                ('equipment_description', models.CharField(blank=True, max_length=100)),
                ('equipment_price', models.IntegerField()),
                ('equipment_image', models.ImageField(upload_to='shared_equipment_image')),
                ('euipment_pincode', models.IntegerField()),
                ('equipment_contact', models.IntegerField()),
                ('equipment_date', models.DateField(auto_now_add=True)),
                ('equipment_time', models.TimeField(auto_now_add=True)),
                ('no_of_equipment', models.IntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.farmer')),
            ],
            options={
                'verbose_name_plural': 'Shared Equipment',
            },
        ),
    ]
