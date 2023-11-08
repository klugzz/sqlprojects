from django.shortcuts import render
from sqlapp.models import Product
def read(request):
	product=Product.objects.all()
	return render(request,'apps/home.html',{'s':product})
# Create your views here.
