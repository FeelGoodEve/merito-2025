from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app_scinet.decorators import group_required
from app_scinet.forms.ArticleForm import ArticleForm
from app_scinet.forms.CommentForm import CommentForm
from app_scinet.models import Article, Interaction
from app_scinet.forms import CustomUserRegistrationForm


def index_page(request):
    articles = Article.objects.all().order_by('-created_at')

    # Przechodzimy przez wszystkie artykuły pobrane wcześniej z bazy danych
    for article in articles:

        # Tworzymy nowy atrybut `like_count` w obiekcie `article`
        # Wartość to liczba interakcji typu 'like' związanych z tym artykułem
        article.like_count = Interaction.objects.filter(article=article, type='like').count()

        # Tworzymy nowy atrybut `comment_count` w obiekcie `article`
        # Wartość to liczba interakcji typu 'comment' dla tego artykułu
        article.comment_count = Interaction.objects.filter(article=article, type='comment').count()

        # Sprawdzamy, czy użytkownik jest zalogowany (czyli czy mamy dostęp do `request.user`)
        if request.user.is_authenticated:

            # Tworzymy nowy atrybut `liked_by_user` w artykule
            # Sprawdzamy, czy istnieje w bazie wpis interakcji typu 'like'
            # przypisany do tego artykułu i tego użytkownika
            article.liked_by_user = Interaction.objects.filter(
                article=article,
                user=request.user,
                type='like'
            ).exists()

        else:
            # Jeśli użytkownik nie jest zalogowany, ustawiamy `liked_by_user` na False
            article.liked_by_user = False

    # Tworzymy słownik `context`, który przekażemy do szablonu
    # Zawiera on listę artykułów z dodatkowymi atrybutami (lajki, komentarze, polubienia użytkownika)
    context = {
        'articles': articles
    }

    return render(request, 'main.html', context)


def article_page(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Interaction.objects.filter(article=article, type='comment').order_by('created_at')
    comment_form = CommentForm()

    context = {'article': article, 'comment_form': comment_form, 'comments': comments}


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


@login_required
def unlike_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    # Znajdź interakcję typu 'like' dla tego użytkownika i artykułu
    like = Interaction.objects.filter(
        user=request.user,
        article=article,
        type='like'
    ).first()

    # Usuń ją jeśli istnieje
    if like:
        like.delete()

    return redirect('home')  # albo np. 'article' z powrotem



# Widok obsługujący komentowanie artykułu
@login_required
def comment_article(request, article_id):
    # Jeśli metoda jest inna niż post - przekierowanie na stronę główną
    if request.method != 'POST':
        return redirect('home')
    #jeśli nie ma takiego artykułu to 404
    article = get_object_or_404(Article, pk=article_id)
    form = CommentForm(request.POST)

    # Sprawdzamy, czy formularz jest poprawny
    if form.is_valid():
        # Jeśli formularz jest poprawny, tworzymy nową interakcję
        Interaction.objects.create(
            user=request.user,
            article=article,
            type='comment',
            # Używamy form.cleaned_data['content'], aby uzyskać treść komentarza
            #cleanded_data to słownik, który zawiera tylko poprawne dane
            #te dane są walidowane przez formularz
            content=form.cleaned_data['content']
        )
    # Po dodaniu komentarza przekierowujemy użytkownika z powrotem na stronę artykułu
    return redirect('article', article_id=article_id)


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # przypisz autora
            article.save()
            return redirect('home')  # możesz zmienić np. na redirect('article', article_id=article.id)
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})