from django.shortcuts import render, redirect
from django.views import View
from .models import student
from .form import addstudentForm

class Home(View):
    def get(self, request):
        stu_data= student.objects.all()
        return render(request , 'core/home.html',{'studata':stu_data})
    
class Add_student(View):

    def get(self,request):
        fm = addstudentForm()
        return render(request, 'core/add-student.html', {'form':fm})  

    def post(self,request):
        fm = addstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
           return render(request, 'core/add-student.html', {'form':fm})  

class Delete_Student(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        studata = student.objects.get(id=id)
        studata.delete()
        return redirect('/')

class Edit_Student(View):
    def get(self,request,id):
        stu = student.objects.get(id=id)
        fm = addstudentForm(instance=stu)
        return render(request,'core/edit-student.html',{'form':fm})
    
    def post(self,request,id):
        stu = student.objects.get(id=id)
        fm = addstudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')

# Create your views here.
