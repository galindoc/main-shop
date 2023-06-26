# Generated by Django 4.2.3 on 2023-07-24 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
        migrations.RemoveField(
            model_name='content',
            name='text',
        ),
        migrations.RemoveField(
            model_name='contenttext',
            name='button',
        ),
        migrations.RemoveField(
            model_name='section',
            name='contents',
        ),
        migrations.AddField(
            model_name='button',
            name='content_text',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='buttons', to='sections.contenttext'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='sections.section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contentimage',
            name='content',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='image', to='sections.content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contenttext',
            name='content',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='text', to='sections.content'),
            preserve_default=False,
        ),
    ]
