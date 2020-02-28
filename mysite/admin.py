from django.contrib import admin
from .models import Client, Event
from import_export.admin import ImportExportModelAdmin



@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
	pass


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
	pass