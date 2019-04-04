from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.GetMain.as_view(), name="main_page"),
]
