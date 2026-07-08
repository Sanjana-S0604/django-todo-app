from django.shortcuts import render,redirect
from.models import TaskModel,CompleteModel,TrashModel


# Create your views here.
def home(request):
    data=TaskModel.objects.all()

    return render(request,'home.html',{'data':data})

def add(request):

    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']

    

        TaskModel.objects.create(
             title=title,
             desc=desc
        )
        return redirect('home')
    
    return render(request,'add.html')

def completed(request):
    data=CompleteModel.objects.all()
    return render(request,'completed.html',{'data':data})

def trash(request):
    data=TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})

def about(request):
    return render(request,'about.html')

def update(request,pk):
    data=TaskModel.objects.get(id=pk)
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        data.title=title
        data.desc=desc
        data.save()
        return redirect('home')
    

        



    return render(request,'update.html' ,{'data':data})


def hcomplete(request,pk):
       data=TaskModel.objects.get(id=pk)
       CompleteModel.objects.create(
           title=data.title,
           desc=data.desc
       )
       data.delete()
       return redirect('home')

def hdelete(request,pk):
    data=TaskModel.objects.get(id=pk)
    TrashModel.objects.create(
        title=data.title,
        desc=data.desc
    )
    data.delete()
    return redirect('home')


def hcomplete_all(request):
    data=TaskModel.objects.all()
    for i in data:
        CompleteModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('completed')


def hdelete_all(request):
    data=TaskModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('trash')
def crestore(request,pk):
    data=CompleteModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=data.title,
        desc=data.desc

    )
    data.delete()
    return redirect('completed')

def cdelete(request,pk):
    data=CompleteModel.objects.get(id=pk)
    TrashModel.objects.create(
        title=data.title,
        desc=data.desc

    )
    data.delete()
    return redirect('completed')

def crestore_all(request):
    data=CompleteModel.objects.all()
    for i in data:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')

def cdelete_all(request):
    data=CompleteModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')

def trestore(request,pk):
    data=TrashModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=data.title,
        desc=data.desc

    )
    data.delete()
    return redirect('home')


def trestore_all(request):
    data=TrashModel.objects.all()
    for i in data:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('home')

def tdelete(request,pk):
    data=TrashModel.objects.get(id=pk)
    data.delete()
    return redirect('trash')

def tdelete_all(request):
    data=TrashModel.objects.all()
    data.delete()
    return redirect('trash')













