from django.urls import path
from .views import IndexView, EventDetailView, delete_client, delete_event

urlpatterns= [
    path('', IndexView.as_view(), name='index'),
    path('event/<int:event_id>', EventDetailView.as_view(), name='event_detail'),
    # path('event/<int:event_id>/<int:client_id>', ClientChangeForm.as_view(), name='change_client'),
    path('event/delete_client/<int:client_id>', delete_client, name='delete_client'),
    path('event/delete_event/<int:event_id>', delete_event, name='delete_event'),
]