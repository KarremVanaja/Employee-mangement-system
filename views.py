#views.py file manages the business logic
# render() loads HTML file
# redirect() avoids duplicate from submission
# get_object_or_404() prevents app crash if ID not found

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# Display all employees
def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employees/employee_list.html', {'employees': employees})


# Add new employee
def employee_create(request):
    if request.method == 'POST':
        # Create employee using form data
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            salary=request.POST['salary'],
            joined_date=request.POST['joined_date']
        )
        return redirect('employee_list')  # Redirect after saving
    return render(request, 'employees/employee_form.html')


# Update existing employee
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.joined_date = request.POST['joined_date']
        employee.save()   # Save updated data
        return redirect('employee_list')

    return render(request, 'employees/employee_form.html', {'employee': employee})


# Delete employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()  # Remove record
        return redirect('employee_list')

    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
