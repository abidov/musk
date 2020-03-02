from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView 
from .forms import ClientForm, EventForm, MessageForm, DocumentForm
from .models import Client, Event, Document
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime
import os
from django.conf import settings
import csv
from django.urls import reverse, reverse_lazy




class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form_event = EventForm()
            for event in Event.objects.all():
                if datetime.datetime.strptime(f'{event.event_date} {event.event_time}', '%Y-%m-%d %H:%M:%S') < datetime.datetime.now():
                    event.active = False
                    event.save()
            events = Event.objects.filter(user=request.user, active=True).order_by('event_date', 'event_time')
            events_count = events.count()
            return render(request, 'home/index.html', {'events': events,
                                                       'form_event': form_event,
                                                       'events_count': events_count,
                                                       }
                          )
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

class UpdateEvent(UpdateView):
    template_name = "home/edit.html"
    model = Event
    form_class = EventForm

    def get_success_url(self):
        return reverse('index')

    # def get(self, request):
    #     form = EventForm(instance=self.object)

    # def post(self, request):
    #     form = EventForm(instance=self.request.POST)
    #     return redirect('index')



class EventDetailView(View):
    def get(self, request, event_id):
        if request.user.is_authenticated:
            doc_form = DocumentForm()
            form_client = ClientForm()
            form_send = MessageForm()
            event = Event.objects.get(pk=event_id, user=request.user)
            clients = Client.objects.filter(user=request.user, event=event)
            clients_count = clients.count()
            return render(request, 'home/event_detail.html', {'clients': clients,
                                                              'form_client': form_client,
                                                              'event': event,
                                                              'form_send': form_send,
                                                              'clients_count': clients_count,
                                                              'form': doc_form
                                                              }
                          )
        return redirect('login')

    def post(self, request, event_id):
        if request.user.is_authenticated:
            event = Event.objects.get(pk=event_id, user=request.user)
            Client.objects.create(user=request.user,
                                  name=request.POST.get('name'),
                                  last_name=request.POST.get('last_name'),
                                  birth_date=request.POST.get('birth_date'),
                                  phone_number=request.POST.get('phone_number'),
                                  email=request.POST.get('email'),
                                  event=event
                                  )
            return redirect('event_detail', event_id=event_id)
        return redirect('login')

class SendMessageView(View):
    def get(self, request, event_id):
        message_form = MessageForm()
        event = Event.objects.get(user=request.user, pk=event_id)
        return render(request, 'home/send_form.html', {'message_form': message_form,
                                                       'event': event
                                                       }
                      )

    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id, user=request.user)
        clients = Client.objects.filter(user=request.user, event=event)
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            html_message = render_to_string('send/email_template.html', {'event': event, 'message': message})
            plain_message = strip_tags(html_message)
            mail.send_mail(subject, plain_message, 'adidovvv.arslan@gmail.com', [client.email for client in clients], html_message=html_message)
            return redirect('index')


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


def model_form_upload(request, event_id):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            with open(settings.BASE_DIR + '/media/' + str(request.FILES.get('document'))) as f:
                reader = csv.reader(f)
                for row in reader:
                    Client.objects.create(user=request.user,
                                          name=row[0],
                                          last_name=row[1],
                                          birth_date=row[2],
                                          phone_number=row[3],
                                          email=row[4],
                                          event=Event.objects.get(user=request.user,
                                                                  pk=event_id),
                                          )
    else:
        form = DocumentForm()
    return redirect('event_detail', event_id)