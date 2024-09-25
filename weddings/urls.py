from django.urls import path
from . import views

urlpatterns = [
    path('wedding-site/<slug:unique_name>/home/', views.wedding_home, name='wedding_home'),
    path('wedding-site/<slug:unique_name>/access/', views.wedding_access, name='wedding_access'),
    path('wedding-site/<slug:unique_name>/faq/', views.wedding_faq, name='wedding_faq'),
    path('wedding-site/<slug:unique_name>/guest-upload/', views.guest_photo_upload, name='guest_photo_upload'),
]
