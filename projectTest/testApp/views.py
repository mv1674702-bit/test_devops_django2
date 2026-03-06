from django.shortcuts import render, redirect
from testApp.models import Tableone

def home(request):
    user_data=Tableone.objects.all()
    if request.method =='POST':
        name = request.POST.get('var_name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        #file
        file=request.FILES.get('file')
        # print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
        Tableone.objects.create(name= name, mobile= mobile, email= email, file= file)
        return redirect("/")
    return render(request, 'home.html', {"data": user_data})