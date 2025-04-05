# Projekt portal SCiNET  
1. Klonowanie projektu

```sh
git clone https://github.com/CuriousCocainist/merito-2025.git
```

2. Tworzenie wirtualnej zmiennej środowiskowej
```shell
python -m venv .venv
```

3. Aktywacja zmiennej środowiskowej
```shell
.venv/Scripts/activate
```

4. Instralacja pakietów / paczek
```shell
pip install -r requirements.txt
```
5. Stworzenie / podłączenie bazy danych postgresql
   - stworzenie pliku .env
   - skopiowanie zawartości z pliku .env.example
   - wklejenie zawartości do pliku .env
   - uzupełnienie od dane lokalne (Twoje dane konfiguracyjne)

Wywołanie migracji (podstawowej)
```shell
python manage.py migrate
```

