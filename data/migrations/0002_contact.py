# Generated by Django 3.2.25 on 2024-12-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cemail', models.CharField(max_length=100)),
                ('cmessage', models.TextField()),
            ],
        ),
    ]