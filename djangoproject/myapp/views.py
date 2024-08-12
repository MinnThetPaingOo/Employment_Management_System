from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import date as dt_date
from .forms import ItemForm
from .models import Employee, Department


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_item(request):
    items = Employee.objects.all()
    return render(request,'all.html',{"items":items})

def salary(request):
    items = Employee.objects.filter(Salary__gte=300000, Salary__lte=500000)
    return render(request,'all.html',{"items":items})

def accounting(request):
    dept = get_object_or_404(Department, DeptName="Accounting")
    print(dept)
    items = Employee.objects.filter(DeptId=dept)
    return render(request, 'all.html', {"items": items})


def date(request):
    start_date = dt_date(2023, 1, 1)
    end_date = dt_date(2023, 12, 31)

    items = Employee.objects.filter(HireDate__range=[start_date, end_date])

    return render(request, 'all.html', {"items": items})

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all')  # Replace 'success_url' with the URL to redirect after successful form submission
    else:
        form = ItemForm()
    return render(request, 'create.html', {'form': form})