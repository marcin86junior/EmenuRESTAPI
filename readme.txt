emenuREST_app
===========

Wymagania:

    Python 3.8.x

Instalacja:

    nagraj pythona 3.8.x
    stwórz folder "PythonRestEmenu"
    wybierz interpreter w programie np.Visual Studio - Python 3.8
    python -m venv myvenv 		- instalacja środowiska
    cd .\myvenv\Scripts\
    activate				- aktywacja nowego środowiska
    pip install --upgrade pip 		- instalacja najnowszej wersji pip
    pip install -r requirements.txt     - instalacja modółów do środowiska
    django-admin startproject myproject
    paste app: "eMenu" (from github) to \myproject\
    
    add in settings.py / INSTALLED_APPS = [
    'rest_framework',
    'django_filters',
    'eMenu',
    
     oraz

dodaj na końcu settings.py:
	
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # 'data' is my media folder
	STATIC_URL = '/static/'
	MEDIA_URL = '/media/'

	REST_FRAMEWORK = {
	    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	    'PAGE_SIZE': 10
	}

	#REST_FRAMEWORK = {
	    #'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
	#}

-----

Migracja + sprawdzenie:

	python.exe .\manage.py migrate    
	python.exe .\manage.py runserver

Dodaj do urls w projekcie:

	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    #path('', include('booksapi.urls')),
	    path('', include('eMenu.urls')),
	]

----- 

Dodaj usera:

    python.exe .\manage.py createsuperuser

Uruchomienie aplikacji:

    python.exe .\manage.py runserver

Dodaj fixturki:

    python  manage.py loaddata eMenu\fixtures\data.json --app eMenu

Testowanie:

    .........................

emenu_app (stare nie aktualne)
===========

API publiczne:
-> Wyświetlanie kart menu tylko z przepisami działa połowicznie dobrze. Po zmianie powiązań class CardItems) wymaga zrestartowania serwera. Wiem, że jest coś takiego jak serializers.update i save - ale nie wiem jak tego używać.

Api niepubliczne:
-> Po zalogoawniu na głównej stronie są udostępniane przyciski do dodawania i edcji: Menu / Dań / Powiązań.
-> Jest możliowść filtroawia wg dowolnego parametru.

Fixtures:
-Polskie jedzenie powiązane z Kotlet schabowy,
-Tajladzkie jedzenie powiązane z Tikimarsala,
-Menu puste bez powiązania z żadnym daniem
-Danie "Zupa ogórkowa" nie przypisane do żadnego menu.

->Raportowanie nie działa (nie umiem Celery)
->Proste 2 testy (umiem tylko postawy)
->Dodawianie obraków do /static działa ale nie skonfigrowałem URLs do wyświetlania
->PostgreSQL - można zmienić linjek w settings.py
->Docker mam nagrany ale jeszcze za bardzo nie umiem
