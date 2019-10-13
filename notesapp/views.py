from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import teacher
from .models import student

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,'notesapp/index.html')


def troute(request):
    return render(request,'notesapp/facultylogin.html')


def sroute(request):
    return render(request,'notesapp/studentlogin.html')

def tlogin(request):
    uname=request.POST.get("username")
    password=request.POST.get("password")
    obj=teacher.objects.filter(username="kiran")
    pa=""
    for i in obj:
        pa=i.password
    print(pa)
    if pa == password:
        return render(request,'notesapp/upload.html')
    else:
         return HttpResponse("<h1> password didn't match </h1>")
def slogin(request):
    uname=request.POST.get("username")
    password=request.POST.get("password")
    obj=student.objects.filter(username=uname)
    pa=obj.password
    if pa in password:
        return render(request,'notesapp/upload.html')
    else:
         return HttpResponse("<h1> password didn't match </h1>")
    return render(request,'notesapp/files.html')

def tregister(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    uname=request.POST.get('username')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    if(cpassword!=password):
        return HttpResponse("<h1> password didn't match </h1>")
    else:
        obj=teacher()
        obj.firstname=fname
        obj.lastname=lname
        obj.username=uname
        obj.password=password
        obj.save()
        return render(request,"notesapp/f_success.html")

def sregister(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    uname=request.POST.get('username')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    if(cpassword!=password):
        return HttpResponse("<h1> password didn't match </h1>")
    else:
        obj=student()
        obj.firstname=fname
        obj.lastname=lname
        obj.username=uname
        obj.password=password
        obj.save()
        return render(request,"notesapp/s_success.html")


context={}
def upload(request):
    if request.method=='POST':
        
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        s=fs.url(name)
        context['url']=s

        print(fs.url(name))
    return render(request,'notesapp/upload.html',context)

def upload_success(request):
    return HttpResponse("<h1> Uploaded Successfully ... </h1>")