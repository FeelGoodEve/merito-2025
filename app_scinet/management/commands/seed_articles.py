from django.core.management.base import BaseCommand
from app_scinet.models import Article


class Command(BaseCommand):
    help = "Czyści tabelę Article i tworzy przykładowe artykuły"

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        self.stdout.write(self.style.WARNING("Wyczyszczono tabelę Article."))

        articles = [
            {
                "title": "Tytuł artykułu 1",
                "content": "Przykładowy artykuł o sztucznej inteligencji i jej zastosowaniach w różnych dziedzinach..."
                           "Przykładowy artykuł o sztucznej inteligencji i jej zastosowaniach w różnych dziedzinach..."
                           "Przykładowy artykuł o sztucznej inteligencji i jej zastosowaniach w różnych dziedzinach..."
                           "Przykładowy artykuł o sztucznej inteligencji i jej zastosowaniach w różnych dziedzinach..."
            },
            {
                "title": "Tytuł artykułu 2",
                "content": "Jakiś tekst o nauce i technologii, który może być interesujący dla czytelników..."
                           "Jakiś tekst o nauce i technologii, który może być interesujący dla czytelników..."
                           "Jakiś tekst o nauce i technologii, który może być interesujący dla czytelników..."
            },
            {
                "title": "Tytuł artykułu 3",
                "content": "Nie mam pomysłu na treść, ale to jest przykładowy artykuł o czymś ważnym... i może być ciekawy. i jeszcze coś..."
                           "Nie mam pomysłu na treść, ale to jest przykładowy artykuł o czymś ważnym... i może być ciekawy. i jeszcze coś..."
                           "Nie mam pomysłu na treść, ale to jest przykładowy artykuł o czymś ważnym... i może być ciekawy. i jeszcze coś..."
                           "Nie mam pomysłu na treść, ale to jest przykładowy artykuł o czymś ważnym... i może być ciekawy. i jeszcze coś..."
            },
        ]

        for article in articles:
            Article.objects.create(
                title=article["title"],
                content=article["content"]
            )

        self.stdout.write(self.style.SUCCESS("Dodano przykładowe artykuły"))
