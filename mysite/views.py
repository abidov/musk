from django.shortcuts import render, redirect
from django.views import View
from .models import Client, Event
# Create your views here.
from users.decorators import logged_only
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return render(request, 'home/index.html')