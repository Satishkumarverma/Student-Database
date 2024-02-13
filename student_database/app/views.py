from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages
from django.http import HttpResponse
import csv
import io
from django.db.models import Q

def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        find = search[:1].upper() + search[1:]
        my_data = Student.objects.filter(name__contains=find) 
        total_student = len(Student.objects.filter(name__contains=find))
        arrow = 'fa-circle-arrow-left'
    else:    
        my_data = Student.objects.all()
        total_student = len(Student.objects.all())
        arrow = ''
    context={
        'my_data':my_data,
        'total_student': total_student,
        'arrow': arrow,
    }
    return render(request, 'app/home.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Details has been Added Successfully!!!')
            return redirect('add_student')
    else:
        form = StudentForm() 
    context={
        'form': form,
    }
    return render(request, 'app/add_student.html', context)

def about(request):
   
    context={
        
    }
    return render(request, 'app/about.html', context)

def profile(request, id):
    data = Student.objects.filter(id=id)[0]
    context={
        'data': data,
    }
    print(data)
    return render(request, 'app/profile.html', context)

def update(request, id):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            clas = form.cleaned_data['clas']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            image = form.cleaned_data['image']
            Student.objects.filter(id=id).update(name=name,clas=clas,dob=dob,gender=gender,email=email,phone=phone,address=address,state=state)
            messages.success(request, f'{name} record has been Updated Successfully!!!')
            return redirect('home')
    else:
        data = Student.objects.filter(id=id)[0]
        form = StudentForm(instance=data)

    context={
        'form': form,
    }
    return render(request, 'app/update.html', context)

def delete(request, id):
    my_data = Student.objects.filter(id=id)[0]
    print(my_data.name)
    student_name =my_data.name 
    my_data.delete()
    messages.success(request, f'{student_name} Data has been Deleted Successfully!!!')
    return redirect('home')

def filter(request):
    if request.method == 'POST':
        clas = request.POST.get('clas')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        print(clas,gender,state)
        clas_filter = Q(clas=clas) if clas else Q()
        gender_filter = Q(gender=gender) if gender else Q()
        state_filter = Q(state=state) if state else Q()
        combined_filter = clas_filter & gender_filter & state_filter
        my_data = Student.objects.filter(combined_filter)
        total_student = len(Student.objects.filter(combined_filter))
        refresh = 'fa-rotate'
    else:
         my_data = ''
         refresh = ''  
         total_student = 0 
         clas = ''
         gender = ''
         state = ''
    context={
        'my_data':my_data,
        'total_student':total_student,
        'refresh':refresh,
        'clas_v':clas,
        'gender_v': gender,
        'state_v': state,
    }
    return render(request, 'app/filter.html', context)

def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'Invalid CSV FILE')
            return redirect('home') 
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for row in csv.reader(io_string, delimiter=',', quotechar="'"):
            print(row)
            name = row[0]
            clas = row[1]
            dob = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            address = row[6]
            state = row[7]
            Student.objects.create(name=name,clas=clas,dob=dob,gender=gender,email=email,phone=phone,address=address,state=state)
        messages.success(request,'Record has been Added Successfully!!!')
        return redirect('home')
    
    return render(request,'app/csv.html')

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stusent_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'clas', 'dob', 'gender', 'email', 'phone', 'address', 'state', 'image'])
    users = Student.objects.all()
    for user in users:
        writer.writerow([user.name, user.clas, user.dob, user.gender, user.email, user.phone, user.address, user.state, user.image])
    return response




