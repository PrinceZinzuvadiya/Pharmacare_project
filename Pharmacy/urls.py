from django.contrib import admin
from django.urls import path,include
from Pharmacy import views

urlpatterns = [
    path('', views.home),
    path('managerlogin/', views.managerlogin, name='managerlogin'),
    path('managersignup/', views.managersignup, name='managersignup'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminsignup/', views.adminsignup, name='adminsignup'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('managerhome/', views.managerhome, name='managerhome'),
    path('updatemanager/', views.updatemanager, name='updatemanager'),
    path('updateadmin/', views.updateadmin, name='updateadmin'),
    path('allmanager/', views.allmanager, name='allmanager'),
    path('userlogout/',views.userlogout),
    path('medicinelist/', views.medicinelist, name='medicinelist'),
    path('addmedicine/', views.addmedicine),
    path('remove/', views.remove, name='remove'),
    path('removemedicine/<int:id>', views.removemedicine, name='removemedicine'),
    path('edit/', views.edit, name='edit'),
    path('editmedicine/<int:id>', views.editmedicine, name='editmedicine'), 
    path('back/', views.back), 
    path('antibiotics/', views.antibiotics, name='antibiotics'),
    path('Allergy/', views.Allergy, name='Allergy'),
    path('Antacids/', views.Antacids, name='Antacids'),
    path('ColdandFlu/', views.ColdandFlu, name='ColdandFlu'),
    path('Cardiovascular/', views.Cardiovascular, name='Cardiovascular'),
    path('Diabetes/', views.Diabetes, name='Diabetes'),
    path('Dermatological/', views.Dermatological, name='Dermatological'),
    path('Bone/', views.Bone, name='Bone'),
    path('Hormonal/', views.Hormonal, name='Hormonal'),
    path('Gastrointestinal/', views.Gastrointestinal, name='Gastrointestinal'),
    path('Mental/', views.Mental, name='Mental'),
    path('Ophthalmic/', views.Ophthalmic, name='Ophthalmic'),
    path('Pain/', views.Pain, name='Pain'),
    path('Vaccines/', views.Vaccines, name='Vaccines'),
    
]
