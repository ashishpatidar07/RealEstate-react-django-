from django.urls import path
from . import views

urlpatterns = [
    path("residencies/", views.residency_list, name="residency_list"),
    path("contact/", views.contact_create, name="contact_create"),
    path("hello/", views.hello_world, name="hello_world"),
]
