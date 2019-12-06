from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import teacher
from .models import student
from .models import  course
from .models import  filedb
from .models import  studentstats

import os
from django.conf import settings
from django.templatetags.static import static
updatedcourse=''
updatedusername=''
updatedfile=''

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
    obj=teacher.objects.filter(username=uname)
    pa=""
    for i in obj:
        pa=i.password
    print(pa)
    if pa == password:
        return render(request,'notesapp/upload.html')
    else:
         return HttpResponse("<h1> password didn't match </h1>")


def tlogout(request):
    return render(request,'notesapp/facultylogin.html')


def slogin(request):
    uname=request.POST.get("username")
    password=request.POST.get("password")
    obj=student.objects.filter(username=uname)
    
    context={}
    for i in obj:
        context['courses']=list(i.courses[1:-1].split(','))

    for i in obj:
        pa=i.password
    print(pa)
    global updatedusername
    updatedusername=uname
    if pa == password:
       
        return render(request,'notesapp/files.html', context)
    else:
         return HttpResponse("<h1> password didn't match </h1>")
    return render(request,'notesapp/files.html', context)

def slogout(request):
    return render(request,'notesapp/studentlogin.html')

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
    c1=request.POST.get("c1")
    c2=request.POST.get("c2")
    c3=request.POST.get("c3")
    c4=request.POST.get("c4")
    

    if(cpassword!=password):
        return HttpResponse("<h1> password didn't match </h1>")
    else:
        obj=student()
        obj.firstname=fname
        obj.lastname=lname
        obj.username=uname
        obj.password=password
        l=[c1,c2,c3,c4]
        obj.courses=l


        obj.save()
        return render(request,"notesapp/s_success.html")



def upload(request):
    if request.method=='POST':
        filedb1=filedb()
        filedb1.courseid=request.POST.get("cid")
        


        uploaded_file=request.FILES['document']
        filedb1.fileurl="http://127.0.0.1:8000/media/"+uploaded_file.name
        filewithout=list(uploaded_file.name.split('.'))
        filedb1.filecontent=uploaded_file
        filedb1.filename=filewithout[0]
        filedb1.save()
        
        # fs=FileSystemStorage()
        # name=fs.save(uploaded_file.name,uploaded_file)
        # s=fs.url(name)
        # context['url']=s

        # print(fs.url(name))
    return render(request,'notesapp/upload.html')

def upload_success(request):
    return HttpResponse("<h1> Uploaded Successfully ... </h1>")

def add_course(request):
    c1=course()
    c1.courseid=request.POST.get('cid')
    c1.coursename=request.POST.get('cname')
    c1.credits1=request.POST.get('credits')
    c1.coordinator=request.POST.get('coordinator')
    c1.save()
    return HttpResponse("<h2>Course added successfully !!!!</h2>")

def view_course(request):
    cid=request.POST.get('cid')
    print(cid)
    c1=course.objects.filter(courseid=cid)
    context={}
    # print(len(c1))
    global updatedcourse  
    updatedcourse=cid
   

    for c in c1: 
        



        context['cid']=cid
        context['cname']=c.coursename
        context['credits']=c.credits1
        context['coordinator']=c.coordinator
        filesdict={}
        flist=filedb.objects.filter(courseid=cid)
        for i in flist:
            filesdict[i.filename]="http://127.0.0.1:8000/media/"+i.filename
        context['filesdict']=filesdict
        # print(filesdict)
        
        # path=settings.MEDIA_ROOT
        # img_list=os.listdir(path)
        # context['images']=img_list






    return render(request,'notesapp/courses.html', context)         

from django.urls import resolve

def count(request):
    
    

    
    url1=request.get_full_path()
    urll=list(url1.split('/'))

    
    s=studentstats()
    s1=studentstats.objects.filter(susername=updatedusername).filter( courseid=updatedcourse).filter( filename=urll[-1])
    if not s1:

        s.susername=updatedusername
        s.courseid=updatedcourse
        s.fcount=1
        s.filename=urll[-1]
        s.save()
    else:
        for i in s1:
            i.fcount=i.fcount+1
            i.save()

    filedb1=filedb.objects.filter(filename=urll[-1])
    for i in filedb1:
        i.fcount=i.fcount+1
        i.save()


    print("---------------")
    print(updatedcourse)
    context={}
    context['updatedcourse']=updatedcourse
    context['updatedusername']=updatedusername
    return render(request,"notesapp/status.html",context)

def add_count(request):
    return HttpResponse("<h2>sdjhbfsdf</h2>")



