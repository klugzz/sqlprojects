from django import forms
from sqlapp.models import Employee
class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'