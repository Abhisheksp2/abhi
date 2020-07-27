from django.shortcuts import render
from testApp.models import *

# Create your views here.
from testApp.models import Contact


def home(request):
    return render(request,'testApp/index.html')

def about(request):
    return render(request,'testApp/about.html')

def sample_post(request):
    return render(request,'testApp/post.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        message  = request.POST['message']

        contact_data = Contact(name=name,mail=email,message=message,phonenumber=phone_number)
        contact_data.save()
        my_dict = {'msg':'User added into the system'}
        return render(request, 'testApp/contact.html', context=my_dict)

    return render(request,'testApp/contact.html')



