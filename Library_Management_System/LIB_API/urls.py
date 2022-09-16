from django.urls import path 
from LIB_API import views
from LIB_API.adminEndpoints import admin_Api
from LIB_API.bookEndpoints import book_Api

from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
   
    #admin urls
    
    path('admin/signup',admin_Api.signUp),
    path('admin/login',admin_Api.login),
    
    # book urls
    path('book/newentry',book_Api.newEntry),
    path('book/retrieveall',book_Api.RetrieveAll),
    path('book/update',book_Api.Update),
    path('book/delete',book_Api.Delete),
    path('book/singlebookInfo',book_Api.singleBookInfo),
 
]

