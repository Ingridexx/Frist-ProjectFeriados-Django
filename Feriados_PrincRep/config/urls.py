"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls), #URL do Admin
    # Mapeia a URL /admin/ para o painel de administração do Django
    path('api/', include('holidays.urls')), # URLs da API do app 'holidays'
    # inclui as URLs da API do app holidays sob o prefixo /api/
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # Tela de Login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Tela de LogOut
    # Configura as URLs de login e logout usando as views embutidas do Django
    path('', include('holidays.urls')), #URLs da interface de usuário do app 'holidays
    # Inclui as URLs de interface de usuário do app holidays na raiz do site
]
