"""zsheets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from zapp.views import login

from django.contrib.auth.views import LoginView

from django.urls import include, path

urlpatterns = [
    path('', login, name="default"),
    path('zapp/', include('zapp.urls'), name="zapp"),
    path('admin/', admin.site.urls),  
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name="login"),
    path('accounts/', include('django.contrib.auth.urls'))
]
