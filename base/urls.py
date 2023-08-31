from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home,name="home"),
    path('form/',views.form,name="form"),
    path('delete/<str:pk>/',views.delete,name="delete"),
    path('test/',views.test,name="test"),
]