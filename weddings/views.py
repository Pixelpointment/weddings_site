from django.shortcuts import render, get_object_or_404, redirect
from .models import WeddingSite, GuestPhoto
from .forms import GuestPhotoForm

def wedding_access(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)
    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/wedding_access.html"


    if request.method == 'POST':
        entered_code = request.POST.get('access_code')
        if entered_code == wedding_site.access_code:
            request.session['access_granted'] = unique_name
            return redirect(template_name, unique_name=unique_name)
        else:
            return render(request, 'wedding_access.html', {'error': 'Incorrect access code'})

    return render(request, template_name)


def wedding_home(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    # Construct the template path based on the layout selected
    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/home.html"

    photos = wedding_site.photos.all()
    guest_photos = wedding_site.guest_photos.filter(approved=True)
    faqs = wedding_site.faqs.all()

    return render(request, template_name, {
        'wedding_site': wedding_site,
        'photos': photos,
        'guest_photos': guest_photos,
        'faqs': faqs
    })


def wedding_faq(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/wedding_faq.html"  # Update if you have a specific FAQ template
    
    faqs = wedding_site.faqs.all()

    return render(request, template_name, {
        'wedding_site': wedding_site,
        'faqs': faqs
    })


def guest_photo_upload(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    if request.method == 'POST':
        form = GuestPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            guest_photo = form.save(commit=False)
            guest_photo.wedding_site = wedding_site
            guest_photo.save()
            return redirect('wedding_home', unique_name=unique_name)
    else:
        form = GuestPhotoForm()

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/guest_photo_upload.html"

    return render(request, template_name, {
        'form': form,
        'wedding_site': wedding_site
    })


def wedding_menu(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/guest_photo_upload.html"

    return render(request, template_name, {
        'wedding_site': wedding_site
    })



