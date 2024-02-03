from django.http import Http404 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def managerlogin(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']
        try:
            user = manager.objects.get(username=unm, password=pas)
            messages.success(request, "Login successful")
            request.session["user"] = unm
            request.session["name"] = user.firstname + user.lastname
            request.session["userid"] = user.id
            request.session["user_role"] = "manager" 
            print("User Role:", request.session.get("user_role"))
            return redirect('managerhome')
        except ObjectDoesNotExist:
            messages.error(request, "Login failed: User not found")
    return render(request, 'managerlogin.html')

def managersignup(request):
    if request.method=='POST':
        newuser=managerform(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup succesful.")
            return redirect('managerlogin')
        else:
            print(newuser.errors)
    return render(request, 'managersignup.html')

def updatemanager(request):
    user = request.session.get('user')
    userid = request.session.get('userid')
    if not userid:
        raise Http404("User ID not found in session")
    try:
        cuser = manager.objects.get(id=userid)
    except manager.DoesNotExist:
        raise Http404("User not found")
    if request.method == 'POST':
        updateprofile = updatemanagerform(request.POST, instance=cuser)
        if updateprofile.is_valid():
            updateprofile.save()
            print("Data updated successfully")
            return redirect('managerhome')
        else:
            print(updateprofile.errors)
    return render(request, 'updatemanager.html', {'user': user, 'cuser': cuser})

def userlogout(request):
    logout(request)
    return redirect("/")

# @login_required
def managerhome(request):
    name = request.session.get('name')
    print(f"Name: {name}")
    return render(request, 'managerhome.html', {'name': name})

def medicinelist(request):
    name=request.session.get('name')
    medicines=medicine.objects.all()
    return render (request, 'medicinelist.html', {'name':name, 'medicines':medicines, 'user_role': request.session.get('user_role')})

def addmedicine(request):
    name=request.session.get('name')
    if request.method=='POST':
        newmed=medicineform(request.POST)
        if newmed.is_valid():
            newmed.save()
            print("Data saved succesfully")
        else:
            print(newmed.errors)
    return render (request, 'addmedicine.html', {'name':name, 'user_role': request.session.get('user_role')})

def edit(request):
    name = request.session.get('name')
    med = medicine.objects.all()
    return render(request, 'edit.html', {'name': name, 'med': med, 'user_role': request.session.get('user_role')})

def editmedicine(request,id):
    name=request.session.get('name')
    edit=medicine.objects.get(id=id)
    if request.method=='POST':
        editdata=updatemedicine(request.POST, instance=edit)
        if editdata.is_valid():
            editdata.save()
            print("Data updated")
            return redirect('edit')
        else:
            print(editdata.errors)
    return render (request, 'editmedicine.html', {'name':name, 'edit':edit, 'user_role': request.session.get('user_role')})

def remove(request):
    name = request.session.get('name')
    med = medicine.objects.all()
    return render(request, 'remove.html', {'name': name, 'med': med, 'user_role': request.session.get('user_role')})

def removemedicine(request, id):
    name = request.session.get('name')
    med = get_object_or_404(medicine, id=id)
    med.delete()
    return redirect('remove')

def back(request):
    return redirect ('managerhome')

def antibiotics(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Antibiotics')
    return render(request, 'antibiotics.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Allergy(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Allergy Medications')
    return render(request, 'Allergy.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Antacids(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Antacids')
    return render(request, 'Antacids.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def ColdandFlu(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Cold and Flu')
    return render(request, 'ColdandFlu.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Cardiovascular(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Cardiovascular')
    return render(request, 'Cardiovascular.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Diabetes(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Diabetes')
    return render(request, 'Diabetes.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Dermatological(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Dermatological (Skin)')
    return render(request, 'Dermatological.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Bone(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Bone Health')
    return render(request, 'Bone.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Hormonal(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Hormonal')
    return render(request, 'Hormonal.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Gastrointestinal(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Gastrointestinal')
    return render(request, 'Gastrointestinal.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Mental(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Mental Health')
    return render(request, 'Mental.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Ophthalmic(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Ophthalmic (Eye)')
    return render(request, 'Ophthalmic.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Pain(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Pain Relief')
    return render(request, 'Pain.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def Vaccines(request):
    name = request.session.get('name')
    anti_med=medicine.objects.filter(category='Vaccines')
    return render(request, 'Vaccines.html', {'anti_med':anti_med, 'name':name, 'user_role': request.session.get('user_role')})

def adminlogin(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']
        try:
            user = admins.objects.get(username=unm, password=pas)
            messages.success(request, "Login successful")
            request.session["user"] = unm
            request.session["name"] = user.firstname + user.lastname
            request.session["userid"] = user.id
            request.session["user_role"] = "admin"
            return redirect('adminhome')
        except ObjectDoesNotExist:
            messages.error(request, "Login failed: User not found")
    return render(request, 'adminlogin.html')

def adminsignup(request):
    if request.method=='POST':
        newuser=adminform(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup succesful.")
            return redirect('adminlogin')
        else:
            print(newuser.errors)
    return render(request, 'adminsignup.html')

def adminhome(request):
    name = request.session.get('name')
    print(f"Name: {name}")
    return render(request, 'adminhome.html', {'name': name})

def updateadmin(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    if not userid:
        raise Http404("User ID not found")
    try:
        cuser=admins.objects.get(id=userid)
    except admins.DoesNotExist:
        raise Http404("User id not found")
    if request.method=='POST':
        updateprofile= adminform(request.POST, instance=cuser)
        if updateprofile.is_valid():
            updateprofile.save()
            print("Profile updated succesfully.")
            return redirect ('adminhome')
        else:
            print(updateprofile.errors)
    return render (request, 'updateadmin.html', {'user': user, 'cuser' : cuser})

def allmanager(request):
    name = request.session.get('name')
    managers=manager.objects.all()
    return render (request, 'allmanager.html', {'managers':managers, 'name':name})


