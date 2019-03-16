from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:room_id>/', views.Role.as_view(), name='role'),
    path('<slug:room_id>/ability/', views.Ability.as_view(), name='ability'),
]
