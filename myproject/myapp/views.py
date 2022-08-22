from django.shortcuts import redirect, render
from .forms import Vn2form
from .models import VnModel
from django.contrib import messages


# Create your views here.
# Registration page
def emp_reg(request):
    return render(request, 'myapp/registration.html')


# create employee
def create_emp(request):
    if request.method == 'POST':
        fm = Vn2form(request.POST)
        if fm.is_valid():
            try:
                id = fm.cleaned_data['vn2id']
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['Email']
                age = fm.cleaned_data['Age']
                dj = fm.cleaned_data['DOJ']
                dg = fm.cleaned_data['DOG']
                djob = fm.cleaned_data['Dojob']
                data = VnModel(vn2id=id, name=nm, Email=em, Age=age, DOJ=dj, DOG=dg, Dojob=djob)
                data.save()
                messages.success(request, 'Employee Registration is successfuly!!')
                return redirect('/show/')
            except:
                pass
    else:
        fm = Vn2form()
    return render(request, 'myapp/insert.html', {'form': fm})


# Retrive all data from database
def show_emp(request):
    emp = VnModel.objects.all()
    return render(request, 'myapp/show.html', {'employees': emp})


# UPDATE DATA FROM DATABASE
def update_emp(request, pk):
    employee = VnModel.objects.get(vn2id=pk)
    fm = Vn2form(request.POST, instance=employee)
    if request.method == 'POST':
        if fm.is_valid():
            fm.save()
            return redirect('/show/')
    else:
        employee = VnModel.objects.get(vn2id=pk)
        fm = Vn2form(instance=employee)
    return render(request, 'myapp/edit.html', {'form': fm})


def delete_emp(request, pk):
    employee = VnModel.objects.get(vn2id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('/show/')
    context = {'employee': employee}
    return render(request, 'myapp/delete.html', context)
