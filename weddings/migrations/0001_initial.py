# Generated by Django 4.2.16 on 2024-09-25 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('template_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Layout1WeddingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ceremony', models.TextField(blank=True, null=True)),
                ('reception', models.TextField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('reception_description', models.TextField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='WeddingSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('access_code', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('layout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weddings.layout')),
            ],
        ),
        migrations.CreateModel(
            name='Starter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('wedding_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starters', to='weddings.layout1weddingdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='wedding_photos/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('wedding_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='weddings.weddingsite')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('wedding_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mains', to='weddings.layout1weddingdetails')),
            ],
        ),
        migrations.AddField(
            model_name='layout1weddingdetails',
            name='wedding_site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wedding_details', to='weddings.weddingsite'),
        ),
        migrations.CreateModel(
            name='GuestPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='guest_photos/')),
                ('message', models.TextField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('wedding_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_photos', to='weddings.weddingsite')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('wedding_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='weddings.weddingsite')),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('wedding_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desserts', to='weddings.layout1weddingdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(blank=True, max_length=7, null=True)),
                ('secondary_color', models.CharField(blank=True, max_length=7, null=True)),
                ('accent_color', models.CharField(blank=True, max_length=7, null=True)),
                ('font_color', models.CharField(blank=True, max_length=7, null=True)),
                ('btn_hover_color', models.CharField(blank=True, max_length=7, null=True)),
                ('wedding_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colours', to='weddings.layout1weddingdetails')),
            ],
        ),
    ]
