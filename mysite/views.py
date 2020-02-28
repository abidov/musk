from django.shortcuts import render, redirect
from django.views import View
from .forms import ClientForm, EventForm, CheckBoxForm
from .models import Client, Event
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form_event = EventForm()
            form_checkbox = CheckBoxForm()
            events = Event.objects.filter(user=request.user)
            return render(request, 'home/index.html', {'events': events, 'form_event': form_event, 'form_checkbox': form_checkbox})
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

class EventDetailView(View):
    def get(self, request, event_id):
        if request.user.is_authenticated:
            form_client = ClientForm()
            event = Event.objects.get(pk=event_id, user=request.user)
            clients = Client.objects.filter(user=request.user, event=event)
            return render(request, 'home/event_detail.html', {'clients': clients, 'form_client': form_client, 'event': event})
        return redirect('login')

    def post(self, request, event_id):
        if request.user.is_authenticated:
            event = Event.objects.get(pk=event_id, user=request.user)
            instance = Client.objects.create(user=request.user,
                                             name=request.POST.get('name'),
                                             last_name=request.POST.get('last_name'),
                                             birth_date=request.POST.get('birth_date'),
                                             phone_number=request.POST.get('phone_number'),
                                             email=request.POST.get('email'),
                                             event=event
                                             )
            return redirect('event_detail', event_id=event_id)
        return redirect('login')

def delete_client(request, client_id):
    if request.user.is_authenticated:
        client = Client.objects.filter(pk=client_id,
                                       user=request.user).first()
        client.delete()
        return redirect('event_detail', event_id=client.event.id)
    return redirect('login')

def delete_event(request, event_id):
    if request.user.is_authenticated:
        event = Event.objects.filter(pk=event_id,
                                     user=request.user).first()
        event.delete()
        return redirect('index')
    return redirect('index')
