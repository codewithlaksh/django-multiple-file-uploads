from django.shortcuts import render, redirect
from .models import Image


def home(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            img = Image.objects.create(image=image)
            img.save()
        return redirect('/')
    images = Image.objects.all()
    for i in images:
        print(i)
    context = {
        'images': images
    }
    return render(request, "home.html", context)
