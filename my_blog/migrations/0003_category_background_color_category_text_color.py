# Generated by Django 4.2.6 on 2024-01-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background_color',
            field=models.CharField(default='#sdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='text_color',
            field=models.CharField(default='sdfasdfas', max_length=100),
            preserve_default=False,
        ),
    ]
