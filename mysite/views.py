from django.shortcuts import render, redirect
from django.views import View
from .forms import ClientForm, EventForm
from .models import Client, Event
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form_event = EventForm()
            events = Event.objects.all().filter(user=request.user)
            return render(request, 'home/index.html', {'events': events,'form_event': form_event})
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            form_event = EventForm(request.POST)
            if form_event.is_valid():
                Event.objects.create(name=request.POST.get('name'),
                                     event_date=request.POST.get('event_date'),
                                     event_time=request.POST.get('event_time'),
                                     place=request.POST.get('place'),
                                     price=request.POST.get('price') if request.POST.get('price') else None,
                                     user=request.user)
            return redirect('index')
        else:
            return redirect('login')