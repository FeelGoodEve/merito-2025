from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app_scinet.views.front_pages_view import index_page, article_page, article_page_p, login_page, user_register_page, \
    logout_page, like_article, unlike_article, comment_article, add_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('article/<int:article_id>', article_page, name='article'),
    path('article-p/<int:article_id>', article_page_p, name='article_p'),
    path('register/', user_register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('unlike/<int:article_id>/', unlike_article, name='unlike_article'),
    path('comment/<int:article_id>/', comment_article, name='comment_article'),
    path('article/add/', add_article, name='add_article'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
