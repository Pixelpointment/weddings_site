from django.contrib import admin
from .models import (
    WeddingSite,
    Layout,
    Photo,
    FAQ,
    GuestPhoto,
    Layout1WeddingDetails,
    Starter,
    Main,
    Dessert,
    Colours,  # Add Colours model to imports
)

# Inline classes for Starters, Mains, Desserts, and Colours
class StarterInline(admin.TabularInline):
    model = Starter
    extra = 1
    verbose_name = "Starter"
    verbose_name_plural = "Starters"

class MainInline(admin.TabularInline):
    model = Main
    extra = 1
    verbose_name = "Main Course"
    verbose_name_plural = "Main Courses"

class DessertInline(admin.TabularInline):
    model = Dessert
    extra = 1
    verbose_name = "Dessert"
    verbose_name_plural = "Desserts"

# Inline class for Colours model
class ColoursInline(admin.TabularInline):
    model = Colours
    extra = 1
    verbose_name = "Colour Scheme"
    verbose_name_plural = "Colour Schemes"

# Inline class for Layout1WeddingDetails
class Layout1WeddingDetailsInline(admin.TabularInline):
    model = Layout1WeddingDetails
    extra = 1
    fields = ('date', 'ceremony', 'reception', 'time', 'reception_description')

# Inline classes for Photos and FAQs
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_name')

@admin.register(WeddingSite)
class WeddingSiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'unique_name', 'layout')
    inlines = [Layout1WeddingDetailsInline, PhotoInline, FAQInline]  # Include only direct relations

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Dynamically populate the layout choices
        form.base_fields['layout'].queryset = Layout.objects.all()
        return form

@admin.register(Layout1WeddingDetails)
class Layout1WeddingDetailsAdmin(admin.ModelAdmin):
    list_display = ('date', 'ceremony', 'reception', 'time')
    inlines = [StarterInline, MainInline, DessertInline, ColoursInline]  # Add all the related inlines here

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('wedding_site', 'image')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('wedding_site', 'question', 'answer')

@admin.register(GuestPhoto)
class GuestPhotoAdmin(admin.ModelAdmin):
    list_display = ('wedding_site', 'uploaded_at', 'approved')
    list_filter = ('approved', 'wedding_site')
    actions = ['approve_photos']

    def approve_photos(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected photos have been approved.")
    approve_photos.short_description = "Approve selected photos"

@admin.register(Starter)
class StarterAdmin(admin.ModelAdmin):
    list_display = ('wedding_details', 'description')

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('wedding_details', 'description')

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('wedding_details', 'description')

# Register the Colours model in the admin panel
@admin.register(Colours)
class ColoursAdmin(admin.ModelAdmin):
    list_display = ('wedding_details', 'primary_color', 'secondary_color', 'accent_color', 'font_color', 'btn_hover_color')
