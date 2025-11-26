"""
URL configuration for web_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from web_system import views
from django.conf.urls import include
from web_system.views.contato_classe import ContatoView
from web_system.forms.custom_login_form import CustomLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),

    path('relacionamentos/',
         include('relacionamentos.urls'),),

    path('admin/', admin.site.urls),

    #path('funcao/search/', views.buscar, name='funcao_search'),

    path('funcao/contato/',views.contato, name='funcao_contato'),

    path('classe/contato/',ContatoView.as_view(), name='classe_contato'),

    path('accounts/login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=CustomLoginForm)),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/profile/', ProfileView.as_view(), name='profileView')
]

