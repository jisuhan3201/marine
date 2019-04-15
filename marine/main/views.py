from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class GetMain(View):

    def get(self, request):

        return render(request, 'home.html', {})

    def post(self, request):

        email = request.POST

        subject = 'Contact form'
        message = "Sender : " + email.get('name') + "\n" + "Email : " + email.get('address') + "\n" + email.get('content')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['jisu@areha.io',]
        send_mail( subject, message, email_from, recipient_list, fail_silently=False )

        return render(request, 'home.html', {})


class GetAbout(View):

    def get(self, request):

        return render(request, 'about.html', {})


class GetProd(View):

    def get(self, request):

        return render(request, 'prod.html', {})


class GetBuy(View):

    def get(self, request):

        return render(request, 'buy.html', {})


class GetCooperation(View):

    def get(self, request):

        return render(request, 'cooperation.html', {})


class GetContact(View):

    def get(self, request):

        return render(request, 'contact.html', {})