from django.shortcuts import render
from django.views import View
from .models import Client, Event
# Create your views here.

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home/index.html', {'clients': Client.objects.all().filter(user=request.user)})