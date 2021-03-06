"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static 

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_view, name='blog'),
    path('create-post/', views.create_post_view, name='create-post'),
    path('update-post/', views.update_post_view, name='update-post'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('delete-image/<int:id>', views.delete_image, name="delete_image"),
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
