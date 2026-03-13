from django.shortcuts import render, redirect
from students.models import Tableone
# Create your views here.
def registration(request):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        branch = request.POST.get('branch')
        city = request.POST.get('city')

        # print(f"Full Name: {full_name}, Email: {email}, College: {college}, Branch: {branch}, City: {city}")
        Tableone.objects.create(full_name=full_name, email=email, college=college, branch=branch, city=city)
        return redirect("/studentlist")
    return render(request, 'registration.html')

def studentlist(request):
    students = Tableone.objects.all()
    return render(request, 'studentlist.html', {'students': students})


