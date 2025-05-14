from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Article
import os
from django.conf import settings

@login_required  # <-- usuń jeśli dostęp ma być publiczny
def download_article_file(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if not article.file:
        raise Http404("Brak pliku do pobrania.")

    file_path = article.file.path
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    else:
        raise Http404("Plik nie został znaleziony")