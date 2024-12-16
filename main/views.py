from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.templatetags.static import static

def home(request):
    return render(request, 'home.html')

def resume(request):
    filepath = static('resume.pdf')
    with open(filepath, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response

def introduction(request):
    return render(request, 'introduction.html')

def technologies(request):
    return render(request, 'technologies.html')

def certifications(request):
    return render(request, 'certifications.html')

def coding_profiles(request):
    return render(request, 'coding_profiles.html')

def hero_page(request):
    return render(request, 'hero_page.html')
