# Generated by Django 5.1.1 on 2024-09-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='blog_posts', to='blog.topic'),
        ),
    ]
