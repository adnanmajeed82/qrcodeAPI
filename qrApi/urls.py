from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('<int:pk>/',DetailTodo.as_view()),
    path('',ListToDo.as_view()),
    path('create/',CreateTodo.as_view()),
    path('delete/<int:pk>',DeteleTodo.as_view()),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)