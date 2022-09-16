from django.urls import path 
from LIB_WEB import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
   
    #admin urls
    
    path('',views.home),
    path('web/admin/register',views.adminRegister),
    path('web/deletebook/<str:book_id>',views.deleteBook),
    path('web/showallbooks',views.showAllBooks),
    path('web/addbook',views.addBook),
    path('web/updatebook/<str:book_id>',views.updateBook),
    path('web/logout',views.logout),

    path('web/student/bookview',views.studentView),
  
 
]

