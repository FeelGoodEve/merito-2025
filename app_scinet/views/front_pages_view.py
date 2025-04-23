from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app_scinet.decorators import group_required
from app_scinet.models import Article, Interaction
from app_scinet.forms import CustomUserRegistrationForm


def index_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'main.html', context)


def article_page(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}

    return render(request, 'article.html', context)


# PoC
@login_required
@group_required('grupa1')
def article_page_p(request, article_id):
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
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home')
    else:
        form = CustomUserRegistrationForm()

    context = {'form': form}
    return render(request, 'user_register_form.html', context)


def logout_page(request):
    logout(request)
    return redirect("home")


# Widok obsługujący lajkowanie artykułu
@login_required  # Tylko zalogowany użytkownik może lajkować artykuł
def like_article(request, article_id):
    # Importujemy Interaction lokalnie (jeśli nie masz jeszcze importu na górze)
    from app_scinet.models import Interaction

    # Pobieramy artykuł, do którego użytkownik chce dodać lajka
    article = get_object_or_404(Article, pk=article_id)

    # Sprawdzamy, czy użytkownik już wcześniej polubił ten artykuł
    already_liked = Interaction.objects.filter(
        user=request.user,
        article=article,
        type='like'
    ).exists()

    # Jeśli nie ma jeszcze takiej interakcji — tworzymy nowy wpis
    if not already_liked:
        Interaction.objects.create(
            user=request.user,
            article=article,
            type='like'
        )

    # Po dodaniu lajka przekierowujemy użytkownika z powrotem na stronę główną
    return redirect('home')
