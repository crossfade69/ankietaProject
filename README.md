## ankietaProject

## Opis
Aplikacja webowa wykonana w technologii Django do obsługi głosowań elektronicznych wspomagających prowadzenie wykładów na uczelniach wyższych. 

## Wymagania
asgiref==3.7.2
contourpy==1.1.0
cycler==0.12.1
Django~=4.2
django-background-tasks==1.2.5
django-compat==1.0.15
django-user-sessions==2.0.0
django-widget-tweaks==1.5.0
fonttools==4.46.0
kiwisolver==1.4.5
numpy==1.24.2
packaging==23.2
Pillow==10.1.0
pyparsing==3.1.1
python-dateutil==2.8.2
six==1.16.0
sqlparse==0.4.4
tzdata==2023.3
python-dotenv==1.0.0
psycopg2-binary==2.9.5
gunicorn==20.1.0
whitenoise~=6.6.0

Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki, używając:
```bash
pip install -r requirements.txt

## Instalacja
1. Sklonuj repozytorium:
https://github.com/crossfade69/ankietaProject.git

2. Przejdź do katalogu projektu
cd ankietaProject

3. Zainstaluj zależności:
pip install -r requirements.txt

4. Wykonaj migracje bazy danych:
python manage.py migrate

5. Uruchom serwer deweloperski:
python manage.py runserver

Teraz możesz otworzyć przeglądarkę i przejść pod adres http://localhost:8000/, aby zobaczyć swój projekt w działaniu.

## Konfiguracja

Pamiętaj o skonfigurowaniu pliku settings.py zgodnie z Twoimi wymaganiami.
Sprawdź dokumentację Django w celu uzyskania dodatkowych informacji.

## Struktura Katalogów
    /poll: Tutaj znajduje się kod aplikacji Ankieta.
        /management/commands: Komendy zarządzające projektem.
        /migrations: Migracje bazy danych.
        admin.py: Konfiguracja panelu administracyjnego.
        apps.py: Konfiguracja aplikacji.
        forms.py: Formularze dla aplikacji.
        models.py: Modele baz danych.
        views.py: Widoki aplikacji.
    /static: Tutaj znajdują się pliki statyczne projektu.
        style.css: Arkusz stylów dla strony.
    /staticfiles: Tutaj są przechowywane pliki statyczne używane w produkcji.
    /templates/poll: Szablony HTML dla aplikacji Ankieta.
        chart.html: Strona wykresu wyników.
        notready.html: Strona informująca, że ankieta nie jest gotowa.
        panel.html: Panel sterowania.
        password.html: Strona wymagająca hasła.
        thankyou.html: Strona potwierdzająca udane głosowanie.
        unauthorized.html: Strona informująca o braku autoryzacji.
        vote.html: Strona głosowania.
    /registration: Szablony HTML dla rejestracji i logowania użytkowników.
        edit_profile.html: Strona edycji profilu.
        login.html: Strona logowania.
        register.html: Strona rejestracji.
    .gitignore: Plik ignorujący pliki i katalogi w systemie kontroli wersji Git.
    db.sqlite3: Baza danych SQLite.
    manage.py: Skrypt zarządzający projektem Django.
    Procfile: Plik konfiguracyjny dla platformy Heroku.
    requirements.txt: Lista zależności projektu.
    runtime.txt: Wersja Pythona dla platformy Heroku.

## Używane Technologie
    Django
    Python
    SQLite (lub inna baza danych, którą używasz)
    HTML, CSS, JavaScript (lub inne technologie front-endowe)

## Autorzy
Michał Napiórkowski (@crossfade69)



 

