# Generated by Django 5.0.3 on 2024-03-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincontent',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
    ]
