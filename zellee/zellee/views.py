from django.shortcuts import render
from Zell.models import contact,contactus,query

def home(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        qu=query(contact=phone,email=email,message=msg)
        qu.save()
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        qu=contactus(name=name,contact=phone,email=email,message=msg)
        qu.save()
    return render(request,"contact.html")

