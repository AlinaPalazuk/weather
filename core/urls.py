from django.urls import path

from . import views

urlpatterns = [
    path('places/<int:place_id>/', views.place_detail),
]
