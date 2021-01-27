﻿emenuREST_app
===========

Wymagania:

    Python 3.8.x

Instalacja:

	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	python -m venv myvenv
	cd .\myvenv\Scripts\
	.\activate
	cd..
	cd..
	pip install -r requirements.txt
	pip install --upgrade pip 
	pip install django-rest-swagger
	wyłacz w urls.py (w myproject):      #path('', include('eMenu.urls')),
	cd myproject\
	python manage.py migrate
	python manage.py createsuperuser   np.Marcin / hasło: 123
	włacz w urls.py (w myproject):      path('', include('eMenu.urls')),
	python manage.py runserver

Dodawanie fixturek:

	python  manage.py loaddata eMenu\fixtures\data.json --app eMenu

Testy:
	
	.....................

Pokrycie testów:

	.....................


emenu_app (stare nie aktualne)
===========

API publiczne:
...

Api niepubliczne:
...

Fixtures:
-Polskie jedzenie powiązane z Kotlet schabowy,
-Tajladzkie jedzenie powiązane z Tikimarsala,
-Menu puste bez powiązania z żadnym daniem
-Danie "Zupa ogórkowa" nie przypisane do żadnego menu*** (nie dodane)

Wymagane poprawki (ważne):

->dodać raportowanie / Celery+Redis (Heroku)
->dodać testy
->dodać pokrycie testów
->PostgreSQL (sprawdzić czy działa)
->Docker
->Swagger

Małe poprawki:
->logowanie (wyrzuca na główną stronę) - w settings
->małe obraki do potraw
