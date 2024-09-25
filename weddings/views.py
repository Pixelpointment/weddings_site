from django.shortcuts import render, get_object_or_404, redirect
from .models import WeddingSite, GuestPhoto
from .forms import GuestPhotoForm

def wedding_access(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)
    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/wedding_access.html"

    # If no access code is required, skip this view
    if not wedding_site.access_code:
        request.session['access_granted'] = unique_name
        return redirect('wedding_home', unique_name=unique_name)

    # Otherwise, proceed with access code validation
    if request.method == 'POST':
        entered_code = request.POST.get('access_code')
        if entered_code == wedding_site.access_code:
            request.session['access_granted'] = unique_name
            return redirect('wedding_home', unique_name=unique_name)
        else:
            return render(request, 'wedding_access.html', {'error': 'Incorrect access code'})

    return render(request, template_name)


def wedding_home(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    # Check if an access code is required and if access is granted
    if wedding_site.access_code and request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/home.html"

    # Fetch the wedding details
    wedding_details = wedding_site.wedding_details.first()  # Assuming you want the first set of details

    faqs = wedding_site.faqs.all()
    colours = wedding_details.colours.first()

    return render(request, template_name, {
        'wedding_site': wedding_site,
        'wedding_details': wedding_details, 
        'colours': colours, 
        'faqs': faqs
    })


def wedding_faq(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if wedding_site.access_code and request.session.get('access_granted') != unique_name:
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

    if wedding_site.access_code and request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/guest_photo_upload.html"
    if request.method == 'POST':
        form = GuestPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            guest_photo = form.save(commit=False)
            guest_photo.wedding_site = wedding_site
            if wedding_site.photos_need_approval:
                guest_photo.approved = False  # Needs admin approval
            else:
                guest_photo.approved = True  # Auto-approved
            guest_photo.save()
            return redirect('gallery', unique_name=unique_name)
    else:
        form = GuestPhotoForm()
    
    wedding_details = wedding_site.wedding_details.first()  # Assuming you want the first set of details
    colours = wedding_details.colours.first()

    return render(request, template_name, {
        'form': form, 
        'wedding_site': wedding_site,
        'wedding_details': wedding_details, 
        'colours': colours, 
    })

# Photo gallery view (only show approved photos)
def gallery(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if wedding_site.access_code and request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    photos = wedding_site.guest_photos.filter(approved=True)
    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/gallery.html"
    wedding_details = wedding_site.wedding_details.first()  # Assuming you want the first set of details
    colours = wedding_details.colours.first()

    return render(request, template_name, {
        'photos': photos, 
        'wedding_site': wedding_site,
        'wedding_details': wedding_details, 
        'colours': colours, 
    })


def wedding_menu(request, unique_name):
    wedding_site = get_object_or_404(WeddingSite, unique_name=unique_name)

    if wedding_site.access_code and request.session.get('access_granted') != unique_name:
        return redirect('wedding_access', unique_name=unique_name)

    layout_folder = wedding_site.layout.name if wedding_site.layout else 'default_layout'
    template_name = f"{layout_folder}/guest_photo_upload.html"

    return render(request, template_name, {
        'wedding_site': wedding_site
    })



