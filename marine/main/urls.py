from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.GetMain.as_view(), name="main_page"),
    path("about", view=views.GetAbout.as_view(), name="about_page"),
    path("product", view=views.GetProd.as_view(), name="prod_page"),
    path("buy", view=views.GetBuy.as_view(), name="buy_page"),
    path("cooperation", view=views.GetCooperation.as_view(), name="cooperation_page"),
    path("contact", view=views.GetContact.as_view(), name="contact_page"),
]
