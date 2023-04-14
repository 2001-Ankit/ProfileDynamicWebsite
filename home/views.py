from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    my_view ={}
    my_view['reviews'] = Feedback.objects.all()

    return render(request,'index.html',my_view)


def about(request):
    message = {}
    message['reviews'] = Feedback.objects.all()
    message['qualify'] = Qualifications.objects.all()
    message['skills']=Skills.objects.all()
    message['sk'] = SkillRight.objects.all()
    return render(request,'about.html',message)


def contact(request):
    message = {}
    message['informations']=Information.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )

        message['success']="Form is successfully submitted"
        data.save()
        return render(request, 'contact.html', message)

    return render(request,'contact.html',message)


def price(request):

    return render(request,'price.html')


def services(request):

    return render(request,'services.html')


def portfolio(request):

    return render(request,'portfolio.html')


def bhome(request):

    return render(request,'blog-home.html')


def bsingle(request):

    return render(request,'blog-single.html')


def elements(request):

    return render(request,'elements.html')