from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('/users/new/<str:username>/<str:role>',views.users_t,name='users_t'),
        #path('edit_tic/<int:t_id>',views.edit_tic,name='edit_emp'),
      

]
