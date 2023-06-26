# Generated by Django 4.2.3 on 2023-07-24 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_remove_content_image_remove_content_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentimage',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contenttext',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.contentimage'),
        ),
        migrations.AddField(
            model_name='content',
            name='text',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.contenttext'),
        ),
    ]
