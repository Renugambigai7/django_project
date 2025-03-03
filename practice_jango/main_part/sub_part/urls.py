from django.urls import path 

from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('product',views.product,name='product'),
    path('customer',views.customer,name='customer'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    
]

  