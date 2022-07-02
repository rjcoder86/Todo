from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('readcreate',views.ReadCreate.as_view(),name='readcreate' ),
    path('getupdatedelete/<int:pk>',views.GetUpdateDelete.as_view(),name='getupdatedelete' ),
]
urlpatterns+=[
    path('', views.index, name='index'),
    path('addtask', views.addtask, name='addtask'),
    path('deletetask/<int:id>', views.deletetask, name='deletetask'),
    path('updatepage/<str:id>/<str:task>', views.updatepage, name='updatepage'),
    path('updatetask/<int:id>', views.updatetask, name='updatetask')

]