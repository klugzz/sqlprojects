from django.db import models
class Employee(models.Model):
	eno=models.IntegerField()
	name=models.CharField(max_length=64)
	salary=models.IntegerField()
	exp=models.CharField(max_length=256)
# Create your models here.
