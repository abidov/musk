from django.contrib import admin
from .models import Clients
from import_export.admin import ImportExportModelAdmin




@admin.register(Clients)
class ViewAdmin(ImportExportModelAdmin):
	pass

