# Generated by Django 5.1.1 on 2024-11-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, help_text='A banner image for the post', null=True, upload_to=''),
        ),
    ]
