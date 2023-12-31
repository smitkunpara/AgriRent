# Generated by Django 4.2.3 on 2023-07-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_farmerdata_delete_farmers'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('otp_chance', models.IntegerField(default=3)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'All farmers data',
            },
        ),
        migrations.DeleteModel(
            name='farmerdata',
        ),
    ]
