from django.shortcuts import render
from sqlapp.models import Employee
from sqlapp.forms import EmployeeForm
def read(request):
	emp=Employee.objects.all()
	return render(request,'apps/result.html',{'s':emp})
def insert(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	s=Employee.objects.get(id_id)
	s.delete()
	return redirect('/result')
def update(request,id):
	emp=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/result')
	return render(request,'apps/update.html',{'s':emp})

# Create your views here.
