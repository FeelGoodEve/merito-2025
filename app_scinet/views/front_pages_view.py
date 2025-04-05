from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
from app_scinet.models import Article
def index_page(request):

    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'main.html', context)

# @login_required
def article_page(request, article_id):

    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}

    return render(request, 'article.html', context)

def user_register_page(request):
    return render(request, 'user_register_form.html', {
        'is_grid_cols_1': True
    })