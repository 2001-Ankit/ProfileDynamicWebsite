# Generated by Django 4.1.2 on 2023-04-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=20)),
            ],
        ),
    ]