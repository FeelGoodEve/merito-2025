from django.contrib import admin
from django.urls import path
from app_scinet.views.front_pages_view import index_page, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('about/', about_page, name='about'),
]
