"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import Movielist,Moviesitem
from api.views import MovieMList,MovieMItem,UserCreationView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies',Movielist.as_view()),
    # path('movies/<int:mid>',Moviesitem.as_view())
    path('mv/',MovieMList.as_view()),
    path('mv/<int:mid>',MovieMItem.as_view()),
    path('ucv',UserCreationView.as_view())
]
