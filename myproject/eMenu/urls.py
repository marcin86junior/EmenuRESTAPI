from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eMenu import views

router = routers.DefaultRouter()
#public
router.register(r'Card', views.CardListPublic)
router.register(r'Dish', views.DishListPublic)
#not public
router.register(r'CardItems', views.CardItemsList)
router.register(r'DishAuth', views.DishListAuth)
router.register(r'CardItemsAuth', views.CardListAuth)

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', views.homepage),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('lista/', views.ExampleView.as_view()),
    path('schema/', schema_view)
]