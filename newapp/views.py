from django.shortcuts import render,redirect
from newapp.models import addingcategorydb, categorydb , topviewdb
from frontview.models import commentdb,signupdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages







def main_index(request):
    return render(request, "index.html")


def add_cat(request):
    return render(request,"addingcategory.html")

def save_cat(request):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        obj = addingcategorydb(name=na, discription=dis, image=img)
        obj.save()
        messages.success(request,"successfully Added")
        return redirect(add_cat)

def display_category(request):
    data = addingcategorydb.objects.all()
    return render(request,"displaycategory.html",{'data':data})

def edit_category(request,dataid):
    data = addingcategorydb.objects.get(id=dataid)
    return render(request,"edit_category.html",{'data':data})

def update_category(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')

        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name,image)
        except MultiValueDictKeyError:
            file = addingcategorydb.objects.get(id=dataid).image
        addingcategorydb.objects.filter(id=dataid).update(name=na, discription=dis,image=file)
        messages.success(request, "successfully Edited")
        return redirect(display_category)

def delete_category(request,dataid):
    data = addingcategorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "successfully Delete")
    return redirect(display_category)




def items(request):
    data = addingcategorydb.objects.all()
    return render(request, "items.html",{'data':data})


def save_items(request):
   if request.method=="POST":
       ca = request.POST.get('category')
       ma = request.POST.get('movie')
       direc = request.POST.get('director')
       dis = request.POST.get('discription')
       img = request.FILES['movieimage']
       vid = request.FILES['vidio']
       obj = categorydb(category=ca,movie=ma,director=direc,discription=dis,movieimage=img,vidio=vid)
       obj.save()
       messages.success(request, "successfully Saved")
       return redirect(items)



def display_items(request):
    data = categorydb.objects.all()
    return render(request,"displayitem.html",{'data':data})

def edit_items(request,dataid):
    cat = addingcategorydb.objects.all()
    data = categorydb.objects.get(id=dataid)
    messages.success(request, "successfully Edited")
    return render(request,"edititems.html",{'cat':cat,'data':data})

def update_items(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        ma = request.POST.get('movie')
        direc = request.POST.get('director')
        dis = request.POST.get('discription')


        try:
            mov = request.FILES['image']
            fs = FileSystemStorage()
            file1 = fs.save(mov.name, mov)

        except MultiValueDictKeyError:
            file1 = categorydb.objects.get(id=dataid).movieimage
        try:
            vidio = request.FILES['vidio']
            fs = FileSystemStorage()
            file2 = fs.save(vidio.name, vidio)
        except MultiValueDictKeyError:
            file2 = categorydb.objects.get(id=dataid).vidio
        categorydb.objects.filter(id=dataid).update(category=ca,movie=ma,director=direc,discription=dis,movieimage=file1,vidio=file2)
        messages.success(request, "successfully Edited")
        return redirect(display_items)


def delete_items(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "successfully Deleted")
    return redirect(display_items)



def admin_login(request):
    return render(request,"adminlogin.html")


def admin_save(request):
    if request.method=="POST":
        us = request.POST.get('username')
        pa = request.POST.get('password')
        if User.objects.filter(username__contains=us).exists():
            x = authenticate(username=us, password=pa)
            if x is not None:
                login(request, x)
                request.session['username'] = us
                request.session['password'] = pa
                messages.success(request, "successfully Login")
                return redirect(main_index)
            else:
                messages.success(request, "Error...!!!")
                return redirect(admin_login)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "successfully Logout")
    return redirect(admin_login)


def userdisplay(request):
    data = signupdb.objects.all()
    return render(request,"usersignupdetails.html",{'data':data})




def display_comment(request):
    data1 = commentdb.objects.all()
    data = signupdb.objects.all()
    return render(request,"commentdisplay.html",{'data1':data1,'data':data})


def delete_comment(request,dataid):
    data = commentdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "successfully Deleted")
    return redirect(display_comment)


def topview(request):
    return render(request,"topviews.html")

def save_view(request):
    if request.method=="POST":
        ma = request.POST.get('movie')
        direc = request.POST.get('director')
        dis = request.POST.get('discription')
        img = request.FILES['movieimage']
        vid = request.FILES['vidio']
        obj = topviewdb( movie=ma, director=direc, discription=dis, movieimage=img, vidio=vid)
        obj.save()
        return redirect(topview)


def display_view(request):
    view = topviewdb.objects.all()
    return render(request,"displaytopview.html",{'view':view})



def delete_view(request,dataid):
    data = topviewdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "successfully Delete")
    return redirect(display_view)

def enquiry(request):
    data = contactdb.objects.all()
    return render(request,"enquiry.html",{'data':data})

def delete_enq(request,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "successfully Delete")
    return redirect(enquiry)
