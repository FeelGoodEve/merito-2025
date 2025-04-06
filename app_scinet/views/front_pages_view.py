from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
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


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")

        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nieprawidłowy email lub hasło.")

    return render(request, "login.html")

def user_register_page(request):
    return render(request, 'user_register_form.html', {
        'is_grid_cols_1': True
    })