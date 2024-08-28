from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        confirmpassword = request.POST.get("password2")
        if password != confirmpassword:
            messages.warning(request, "Password incorrect")
            return redirect("/signup")

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username is taken")
                return redirect("/signup")
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is taken")
                return redirect("/signup")
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup success, please login")
        return redirect("/login")
    return render(request, "signup.html")


def log_In(request):
    if request.user.is_authenticated:
        return redirect("/index")
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("password1")

        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("/index")
        else:
            messages.error(request, "invalid credentials")
            return redirect("/login")
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def log_out(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect("/login")


def adm(request):
    d = User.objects.all()
    context = {"data": d}
    return render(request, "adm.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        query = User.objects.create_user(username=name, email=email, password=pass1)
        messages.warning(request, "Data inserted successfully")
        query.save()

    d = User.objects.all()
    context = {"data": d}
    return render(request, "adm.html", context)


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        edit = User.objects.get(id=id)
        edit.username = name
        edit.email = email
        edit.save()
        messages.warning(request, "Data Updated successfully")

        return redirect(adm)

    d = User.objects.get(id=id)
    context = {"data": d}
    return render(request, "update.html", context)


def deleteData(request, id):
    d = User.objects.get(id=id)
    d.delete()
    messages.warning(request, "Data deleted successfully")

    return redirect("/adm")
