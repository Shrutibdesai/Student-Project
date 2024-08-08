from django.shortcuts import render,redirect
from studentapp.models import Student

# Create your views here.
def home(request):
    return render(request,'index.html')

def addstudent(request):
    return render(request,'add.html')

def studentlist(request):
   context={}
   data = Student.objects.all()
   print(type(data))
   context['student']=data
   return render(request,'all.html',context)

def saveStudent(request):
   n = request.POST['name']
   e = request.POST['email']
   c = int(request.POST['contact'])
   co= request.POST['course']
   s = Student.objects.create(name=n,email=e,contact=c,course=co)
   s.save()   
   # return render(request,'index.html')
   return redirect('/list')

def deleteStudent(request,sid):
   student = Student.objects.filter(id = sid)
   print(student)
   student.delete()
   return redirect('/list')


def editStudent(request, sid):
   student = Student.objects.filter(id=sid)
   # print(book) # queryset holding a single object
   context={}
   if request.method == "GET":
      # context['book']=book # if we are using get(id=rid)      
      context['student']=student[0] # if wwe are using filter(id=rid)
      return render(request,'edit.html', context)
   else: #POST
      n=request.POST['name']
      e=request.POST['email']
      c=int(request.POST['contact'])
      co=request.POST['course']
      student.update(name=n,email=e,contact=c,course=co) #update can be called on queryset
      return redirect('/list')

