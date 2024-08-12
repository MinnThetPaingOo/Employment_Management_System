from django import forms
from .models import  Employee


class ItemForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['DeptId', 'Name', 'Email', 'Rank', 'Salary','HireDate']