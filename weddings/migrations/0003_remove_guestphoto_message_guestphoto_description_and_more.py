# Generated by Django 4.2.16 on 2024-09-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0002_layout1weddingdetails_hero_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestphoto',
            name='message',
        ),
        migrations.AddField(
            model_name='guestphoto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guestphoto',
            name='uploader_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddingsite',
            name='photos_need_approval',
            field=models.BooleanField(default=True),
        ),
    ]
