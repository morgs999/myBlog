# Generated by Django 5.1.1 on 2024-11-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, help_text='A banner image for the post', null=True, upload_to=''),
        ),
    ]