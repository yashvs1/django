from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django_app.models import contact
from django.contrib.messages import constants as messages
 
# Create your views here.
def index(request):
    
    return render(request, 'django_app/index.html')

def about(request):
    return HttpResponse("this is my about")

def intro(request):
    name = "polyhouse website like IOT"
    context = {'name':name}
    return render(request,'intro.html',context=context)

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact1 = contact(name = name ,email = email, phone = phone ,date = datetime.today())  
        Contact1.save()
        #messages.success(request, 'Profile details updated.')
    return render(request,'contact.html')

