from django.shortcuts import render
from django.contrib import messages
from .forms import *

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
    form = ContactForm()
    data = {
        "forms": form
    }
    return render(request, "mine/index.html", data)