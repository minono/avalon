from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/entry/<slug:room_id>/', consumers.EntryConsumer),
]
