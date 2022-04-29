from django.shortcuts import render,redirect
from .models import *
def student(request):
    s=Student.objects.all()
    if request.method=="POST":
        student.objects.create(
            ism=request.POST.get("ism"),
            yosh=request.POST.get("yosh"),
            kurs=request.POST.get("k"),
            raqam=request.POST.get("r")
        )
        return redirect("/studentlar/")
    return render(request, "student.html",{"studentlar":s})
def reja(request):
    r=Reja.objects.all()
    j=Student.objects.all()
    if request.method=="POST":
        if request.POST.get("b")== False:
            natija=False
        else:
            natija=True
        student.objects.create(
            st=s,
            sana=request.POST.get("sana"),
            bajarilgan=natija,
            raqam=request.POST.get("r")
        )
        return redirect("/rejalar/")
    return render(request, "reja.html",{"reja":r,"student":j})
def student_ochir(request,son):
    Student.objects.get(id=son).delete()
    return redirect("/studentlar/")
def student_edit(request,p):
    if request.method == "POST":
        r = Student.objects.get(id=p)
        r.ism = request.POST.get("i")
        r.raqam = request.POST.get("t")
        r.save()
        return redirect("/studentlar/")
    s=Student.objects.all()
    return render(request, "stu-edit.html", {"student": s})
def reja_edit(request,p):
    if request.method=="POST":
        if request.POST.get("b")== False:
            natija=False
        else:
            natija=True
        r=Reja.objects.get(id=p)
        r.st=request.POST.get("s")
        r.sana=request.POST.get("sana")
        r.bajarilgan=natija
        r.save()
        return redirect("/rejalar/")
    s=Student.objects.get(id=p)
    r=Reja.objects.all()
    return render(request, "reja-edit.html", {"student":s,"reja":r})