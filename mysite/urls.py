from django.urls import path
from .views import IndexView, EventDetailView, delete_client, delete_event, SendMessageView, model_form_upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('', IndexView.as_view(), name='index'),
    path('event/<int:event_id>/', EventDetailView.as_view(), name='event_detail'),
    path('event/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('event/delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('event/send_email_form/<int:event_id>/', SendMessageView.as_view(), name='send_message_form'),
    path('event/save_file/<int:event_id>/', model_form_upload, name='upload'),
]