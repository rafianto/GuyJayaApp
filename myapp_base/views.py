# myapp_base/views.py
from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Halaman Utama',
        'message': 'Selamat datang di aplikasi kami'
    }
    return render(request, 'myapp_base/contents.html', context)