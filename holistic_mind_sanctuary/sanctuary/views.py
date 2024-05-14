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
