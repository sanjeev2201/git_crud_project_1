"""myproject URL Configuration

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.emp_reg,name='emp_reg' ),
    path('create/',views.create_emp,name='insert_emp'),
    path('show/',views.show_emp,name='show_emp'),
    path('edit/<int:pk>',views.update_emp,name='edit_emp'),
    path('remove/<int:pk>',views.delete_emp,name='delete_emp'),
]
