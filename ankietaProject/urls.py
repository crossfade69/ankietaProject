"""
URL configuration for ankietaProject project.

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
from django.urls import path, include

from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('login/', poll_views.teacher_login, name='teacher_login'),
    path('logout/', poll_views.teacher_logout, name='teacher_logout'),
    path('register/', poll_views.teacher_register, name='teacher_register'),
    path('edit_profile/', poll_views.edit_profile, name='edit_profile'),
    path('', poll_views.access, name='access'),
    path('vote/', poll_views.vote, name='vote'),
    path('panel/', poll_views.panel, name='panel'),
    path('chart/', poll_views.chart, name='chart'),
]

