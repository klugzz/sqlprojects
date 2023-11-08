from django.shortcuts import render
from sqlapp.models import Student
def read(request):
	student=Student.objects.all()
	return render(request,'apps/home.html',{'s':student})

# Create your views here.
