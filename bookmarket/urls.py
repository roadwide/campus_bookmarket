from django.contrib import admin
from django.urls import path
from login import views as loginviews
from market import views as marketviews

urlpatterns = [
    path('search/',marketviews.search),
    path('delete/<int:id>',marketviews.delete),
    path('personal/',marketviews.personal),
    path('list/',marketviews.list),
    path('issue/',marketviews.issue),
    path('',loginviews.index),
    path('index/',loginviews.index),
    path('login/',loginviews.login),
    path('register/',loginviews.register),
    path('logout/',loginviews.logout),
    path('admin/', admin.site.urls),
]
