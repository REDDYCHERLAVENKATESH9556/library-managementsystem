from django.urls import path
from librarymanagementsystem.views import index

urlpatterns=[
    path('/index',index)
]
