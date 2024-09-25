import os
from django.conf import settings
from django.db import models


class Layout(models.Model):
    name = models.CharField(max_length=100)
    template_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_available_layouts(cls):
        templates_dir = os.path.join(settings.BASE_DIR, 'weddings/templates')
        layouts = []
        if os.path.isdir(templates_dir):
            for name in os.listdir(templates_dir):
                layout_path = os.path.join(templates_dir, name)
                default_template = f"{name}/default_template.html"
                if os.path.isdir(layout_path) and os.path.isfile(os.path.join(layout_path, 'default_template.html')):
                    layouts.append((name, default_template))
        return layouts


class WeddingSite(models.Model):
    unique_name = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    access_code = models.CharField(max_length=100, blank=True, null=True)  # Access code is now optional
    layout = models.ForeignKey('Layout', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    photos_need_approval = models.BooleanField(default=True)  # New field to control approval setting

    def __str__(self):
        return self.title


class Layout1WeddingDetails(models.Model):
    wedding_site = models.ForeignKey(WeddingSite, related_name='wedding_details', on_delete=models.CASCADE)
    date = models.DateField()
    ceremony = models.TextField(blank=True, null=True)
    reception = models.TextField(blank=True, null=True)
    time = models.TimeField()
    reception_description = models.TextField()
    hero_image = models.ImageField(upload_to='wedding_hero_images/', blank=True, null=True) 

    def __str__(self):
        return f"Wedding details for {self.wedding_site.title}"

    class Meta:
        ordering = ['date']

class Colours(models.Model):
    wedding_details = models.ForeignKey(Layout1WeddingDetails, related_name='colours', on_delete=models.CASCADE)
    primary_color = models.CharField(max_length=7, null=True, blank=True)
    secondary_color = models.CharField(max_length=7, null=True, blank=True)
    accent_color = models.CharField(max_length=7, null=True, blank=True)
    font_color = models.CharField(max_length=7, null=True, blank=True)
    btn_hover_color = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return f"Colours for {self.wedding_details.wedding_site.title}: {self.primary_color}, {self.secondary_color}"


class Starter(models.Model):
    wedding_details = models.ForeignKey(Layout1WeddingDetails, related_name='starters', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Main(models.Model):
    wedding_details = models.ForeignKey(Layout1WeddingDetails, related_name='mains', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Dessert(models.Model):
    wedding_details = models.ForeignKey(Layout1WeddingDetails, related_name='desserts', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Photo(models.Model):
    wedding_site = models.ForeignKey(WeddingSite, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='wedding_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.wedding_site.title}"


class FAQ(models.Model):
    wedding_site = models.ForeignKey(WeddingSite, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ for {self.wedding_site.title}: {self.question}"



class GuestPhoto(models.Model):
    wedding_site = models.ForeignKey(WeddingSite, related_name='guest_photos', on_delete=models.CASCADE)
    uploader_name = models.CharField(max_length=255)  # Name of the guest who uploaded the photo
    photo = models.ImageField(upload_to='guest_photos/')
    description = models.TextField(blank=True, null=True)  # Optional description
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Admin approval status

    def __str__(self):
        return f"{self.uploader_name}'s photo for {self.wedding_site.title}"