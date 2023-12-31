# Generated by Django 4.2.3 on 2023-07-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230706_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('aadharnumber', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=100)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'All Users Data',
            },
        ),
        migrations.DeleteModel(
            name='userdata',
        ),
    ]
