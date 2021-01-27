emenuREST_app
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
