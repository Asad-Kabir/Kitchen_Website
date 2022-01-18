from django.shortcuts import render,HttpResponse
from Home.models import Contact

# Create your views here.

def index(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        detail = request.POST['detail']
        print(name,email,phone,detail)
        contact = Contact(nam=name, email=email, phone=phone, detail=detail)
        contact.save()

    return render(request,"index.html")

def About(request):
     return render(request,"about.html")

def Service(request):
    return render(request,"service.html")

def Contact_us(request):
      return render(request,"contact.html")