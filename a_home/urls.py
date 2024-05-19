from a_home.views import home_view
from django.urls import path

urlpatterns = [
    path("", home_view, name="home"),
]