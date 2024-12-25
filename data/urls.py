from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('update/<int:uk>',views.update_data,name='update'),
    path('details/<int:pk>/', views.details, name='details'),
    path('add/',views.add,name='add'),
    path('delete/<int:pk>',views.delete_data,name='delete'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('con_msg/',views.con_msg,name='con_msg'),
]