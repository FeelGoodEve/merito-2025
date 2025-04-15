from django.contrib import admin
from django.urls import path
from app_scinet.views.front_pages_view import index_page, article_page, article_page_p, login_page, user_register_page, \
    logout_page, like_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('article/<int:article_id>', article_page, name='article'),
    path('article-p/<int:article_id>', article_page_p, name='article_p'),
    path('register/', user_register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('like/<int:article_id>/', like_article, name='like_article'),

]
