from django.shortcuts import render
from app_scinet.models import Article
def index_page(request):

    articles = Article.objects.all()

    context = {'articles': articles}

    return render(request, 'main.html', context)


def about_page(request):

    return render(request, 'article.html')