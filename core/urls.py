from django.urls import path

from . import views

urlpatterns = [
    path('places/', views.place_list, name='place-list'),
    path('places/<int:place_id>/', views.place_detail, name='place-detail'),
]
