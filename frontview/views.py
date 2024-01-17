from django.shortcuts import render,redirect
from newapp.models import addingcategorydb,categorydb,topviewdb
from frontview.models import commentdb,signupdb,contactdb
from django.contrib import messages

# Create your views here.
def front_index(request):
    cat = addingcategorydb.objects.all()
    view = topviewdb.objects.all()
    content = categorydb.objects.all()
    return render(request,"frontindex.html",{'cat':cat,'content':content,'view':view})
def front_content(request):
    cat = addingcategorydb.objects.all()
    fcont = categorydb.objects.all()
    return render(request,"frontcontent.html",{'fcont':fcont,'cat':cat})

def content(request,c_name):
    cat = addingcategorydb.objects.all()
    fcont = categorydb.objects.all()
    rom = categorydb.objects.filter(category=c_name)
    data = addingcategorydb.objects.filter(name=c_name)
    return render(request,"content.html",{'rom':rom,'cat':cat,'data':data,'fcont':fcont})

def single_content(request,dataid):
    cat = addingcategorydb.objects.all()
    single = categorydb.objects.filter(id=dataid)
    comment = commentdb.objects.all()
    return render(request,"singlepage.html",{'cat':cat,'single':single,'comment':comment})


def vidio(request,vidioid):
    cat = addingcategorydb.objects.all()
    vid = categorydb.objects.filter(id=vidioid)
    comment = commentdb.objects.all()
    data = signupdb.objects.all()
    return render(request,"vidio.html",{'cat':cat,'vid':vid,'comment':comment,'data':data})

def login_page(request):
    return render(request,"newlogin.html")



def signin(req):
    return render(req,"newsign.html")

def save_signup(request):
    if request.method=="POST":
        na = request.POST.get('sname')
        email = request.POST.get('semail')
        user = request.POST.get('susername')
        pas = request.POST.get('spassword')
        obj = signupdb(sname=na,susername=user,spassword=pas,semail=email)

        obj.save()
        messages.success(request, "Signed Successfully")
        return redirect(signin)

def user_login(request):
    if request.method=="POST":
        un = request.POST.get('lusername')
        pa = request.POST.get('lpassword')
        if signupdb.objects.filter(susername=un ,spassword=pa).exists():
            request.session['susername']=un
            request.session['spassword']=pa
            messages.success(request, "Login Successfully")
            return redirect(front_index)

        else:
            return redirect(login_page)
    return redirect(login_page)

def userlogout(request):
    del request.session['susername']
    del request.session['spassword']
    messages.success(request, "Logout Successfully")
    return redirect(login_page)


def save_comment(request):
    if request.method=="POST":

        co = request.POST.get('comment')
        obj = commentdb(comment=co)
        obj.save()
        return redirect(front_index)

def intovidio(request):
    return render(request,"intro.html")




def contact_page(req):
    return render(req,"contact.html")


def save_contact(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
    obj = contactdb(name=na,email=em,subject=sub,message=mes)
    obj.save()
    messages.success(request, "Message sent successfully Our Team Will Contact You Shortly")
    return redirect(front_index)


def profile(request):
    prf = signupdb.objects.get(susername=request.session['susername'])

    return render(request,"profile.html",{'prf':prf})