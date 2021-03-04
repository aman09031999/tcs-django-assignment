from django.shortcuts import render, HttpResponse, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def add(request):
    if request.method == "POST":

        r_no = int(request.POST['r_no'])

        try:
            user = Student.objects.get(r_no=r_no)
        except Student.DoesNotExist:
            user = None

            if user is not None:
                return render(request, 'add.html', {'error':'Roll number already exists'})
            else:
                name = str(request.POST['name'])
                dob = request.POST['dob']
                marks = float(request.POST['marks'])
                obj = Student(r_no=r_no, name=name, dob=dob, marks=marks)
                obj.save()
                return render(request, 'view.html', {'lis':Student.objects.all()})
    else:
        return render(request, 'add.html')


def view(request):
    lis = Student.objects.all()
    return render(request, 'view.html', {'lis':lis})


def edit(request, id):
    obj = Student.objects.get(id=id)
    return render(request,'edit.html', {'student':obj})


def update(request, id):
    obj = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("view")
    return render(request, 'view.html', {'student': obj})


def delete(request, id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('view')