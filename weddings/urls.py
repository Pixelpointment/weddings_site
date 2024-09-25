from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<slug:unique_name>/home/', views.wedding_home, name='wedding_home'),
    path('<slug:unique_name>/access/', views.wedding_access, name='wedding_access'),
    path('<slug:unique_name>/faq/', views.wedding_faq, name='wedding_faq'),
    path('<slug:unique_name>/upload-photo/', views.guest_photo_upload, name='guest_photo_upload'),
    path('<slug:unique_name>/gallery/', views.gallery, name='gallery'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
