from django.urls import path
from . import views

urlpatterns = [
    path('registeruser/', views.registeruser, name='registeruser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('myAccount/',views.myAccount,name='myAccount'),
    path('custDashboard/',views.custDashboard,name='custDashboard'),
    path('vendorDashboard/',views.vendorDashboard,name='vendorDashboard'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
]
