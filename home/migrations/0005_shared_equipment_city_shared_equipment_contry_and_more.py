# Generated by Django 4.2.3 on 2023-07-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_shared_equipment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shared_equipment',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shared_equipment',
            name='contry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shared_equipment',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shared_equipment',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shared_equipment',
            name='village',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
