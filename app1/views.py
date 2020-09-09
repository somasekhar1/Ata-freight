from django.shortcuts import render
from .models import Employee_Createrole,Employees_leaves,Manager_Createrole

def employee(request):
    return render(request,'employee.html')
def employee_login(request):
    return render(request, 'employee_login.html')

def emp_login_details(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    login=Employee_Createrole(email=email,password=password)
    if login:
        return render(request,'employee_leave.html')
    else:
        return render(request, 'employee_login.html',{'message':'invaid email or password'})


def employe_register(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    Employee_Createrole(username=username,email=email,password=password).save()
    return render(request,'employee.html',{'message':'successfully create your role'})

def employee_leave(request):
   start_leave_date=request.POST.get('start_leave')
   end_leave_date=request.POST.get('end_leave')
   description=request.POST.get('description')
   total_leaves=request.POST.get('total_leaves')
   Employees_leaves(start_leave_date=start_leave_date,end_leave_date=end_leave_date,description=description,
                    total_leaves=total_leaves,status='pending').save()
   return render(request, 'employee_leave.html', {'message': 'leave applyed successfully'})

def employee_leave_status(request):
    emp=Employees_leaves.objects.all()
    return render(request, 'employee_status.html', {'emp':emp })

def manager(request):
    return render(request,'manager.html')

def manager_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    Manager_Createrole(username=username, email=email, password=password).save()
    return render(request, 'manager.html', {'message': 'successfully create your role'})
def manager_login(request):
    return render(request, 'manager_login.html')
def manager_login_details(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    login = Manager_Createrole(email=email, password=password)
    if login:
        emp = Employees_leaves.objects.all()
        return render(request, 'manager_aprove_leaves.html',{'emp':emp })
    else:
        return render(request, 'manager_login.html', {'message': 'invaid email or password'})

def leave_aprove_status(request):
    id=request.GET.get('emp_aprove_status')
    # print(id)
    employee=Employees_leaves.objects.filter(id=id)
    description=''
    start_leave_date=''
    end_leave_date=''
    total_leaves=''
    if employee:
        for emp in employee:
            description=emp.description
            start_leave_date=emp.start_leave_date
            end_leave_date=emp.end_leave_date
            total_leaves=emp.total_leaves


        return render(request,'leave_aprove_status.html',{'description':description,'start_leave_date':start_leave_date,
                                            'end_leave_date':end_leave_date,'total_leaves':total_leaves})


def employee_leave_success(request):
    start_leave_date = request.POST.get('start_leave')
    end_leave_date = request.POST.get('end_leave')
    description = request.POST.get('description')
    total_leaves = request.POST.get('total_leaves')
    status=request.POST.get('status')
    Employees_leaves(start_leave_date=start_leave_date, end_leave_date=end_leave_date, description=description,
                     total_leaves=total_leaves, status=status).save()
    return render(request, 'leave_aprove_status.html',{'message':'successfully approved '})

