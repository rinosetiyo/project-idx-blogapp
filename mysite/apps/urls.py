from django.urls import path
from apps import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.post_detail, name="single-post")
]