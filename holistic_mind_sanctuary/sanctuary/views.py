from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render
from .models import Zone, Service, Event, Post, BlogPost, EducationalProgram


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
    return render(request, 'sanctuary/services_list.html', {'services': services})


def blog_post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'sanctuary/blog_post_detail.html', {'post': post})


def programs_list(request):
    programs = EducationalProgram.objects.all()
    return render(request, 'sanctuary/programs_list.html', {'programs': programs})
