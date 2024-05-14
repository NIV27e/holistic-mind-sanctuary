from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Service, Event, Post, BlogPost, EducationalProgram


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data, e.g., send an email
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def services_list(request):
    services = Service.objects.all()
    return render(request, 'services_list.html', {'services': services})


def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})


def programs_list(request):
    programs = EducationalProgram.objects.all()
    return render(request, 'programs_list.html', {'programs': programs})

def zones(request):
    zones_info = {
        'social_zone': {
            'title': 'Social Zone',
            'description': 'Dedicated to community interaction and social gatherings, the Social Zone is perfect for '
                           'events, workshops, and public gatherings that foster strong community ties and encourage '
                           'new friendships.',
            'image': 'images/zones/social_zone.jpg'
        },
        'emotional_zone': {
            'title': 'Emotional Zone',
            'description': 'A tranquil area designed for emotional well-being, featuring therapy rooms, quiet spaces, '
                           'and private areas to consult with mental health professionals. It’s an oasis of calm for '
                           'those seeking peace and introspection.',
            'image': 'images/zones/emotional_zone.jpg'
        },
        'environmental_zone': {
            'title': 'Environmental Zone',
            'description': 'Focusing on biophilic design, this zone integrates natural elements into architectural '
                           'and landscape design, promoting environmental education and direct engagement with nature.',
            'image': 'images/zones/environmental_zone.jpg'
        },
        'spiritual_zone': {
            'title': 'Spiritual Zone',
            'description': 'A serene space for meditation, yoga, and spiritual growth, providing a peaceful retreat '
                           'to nurture the soul and enhance spiritual connection in a harmonious environment.',
            'image': 'images/zones/spiritual_zone.jpg'
        },
        'intellectual_zone': {
            'title': 'Intellectual Zone',
            'description': 'Equipped with a library and seminar rooms, this zone supports educational pursuits and '
                           'lifelong learning through classes, workshops, and a comprehensive collection of resources '
                           'on holistic health.',
            'image': 'images/zones/intellectual_zone.jpg'
        },
        'physical_fitness_zone': {
            'title': 'Physical Fitness Zone',
            'description': 'Features state-of-the-art facilities for physical activities such as yoga, Pilates, '
                           'and fitness classes tailored to improve physical health and wellness in a supportive '
                           'setting.',
            'image': 'images/zones/physical_fitness_zone.jpg'
        }
    }
    return render(request, 'zones.html', {'zones': zones_info})
