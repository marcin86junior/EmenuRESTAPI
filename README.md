EmenuRESTAPI 
===========

Wymagania:

    Python 3.8.x

Instalacja:

	utwórz nowy katalog "PythonRestEmenu" i wejdz do niego
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	wyłacz w urls.py (w myproject\myproject):      #path('', include('eMenu.urls')),
	cd myproject\
	python manage.py migrate
	python manage.py createsuperuser
	włacz w urls.py (w myproject\myproject):      path('', include('eMenu.urls')),
	python manage.py runserver

Dodawanie fixturek:

	python  manage.py loaddata eMenu\fixtures\data.json --app eMenu

Testy:
	
	.....................

Pokrycie testów:

	.....................

EmenuRESTAPI (informacje)
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

	->logowanie - przestawić na głowną stronę w settings
	->małe obraki do potraw 
