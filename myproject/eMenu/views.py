from django.http.response import HttpResponse
from django.shortcuts import render, redirect, render
from .models import Dish, Card, CardItems

from rest_framework import viewsets, generics, permissions
from rest_framework import filters
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from eMenu.serializers import EmenuSerializer, EmenuSerializer2, EmenuSerializer3
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.

def homepage(request):
    return render(request, 'eMenu/homepage.html')

class DishListPublic(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = Dish.objects.all()
    serializer_class = EmenuSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self):
        queryset = Dish.objects.all().name('id')
        return queryset

class DishListAuth(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = Dish.objects.all()
    serializer_class = EmenuSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class CardListPublic(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    #script create list of all menu with "dish/es" from conection model CardItems and delete replicated elemnets

    powiazania = CardItems.objects.all()
    #print(list(powiazania))
    listx=list(powiazania)
    j=0
    for i in listx:
        listx[j]=str(listx[j])
        j+=1
    res = [] 
    for i in listx: 
        if i not in res: 
            res.append(i) 
    #print(str(res)+str(' how many: ')+str(len(res)))

    #script is adding do queryset objects "all menu with dishes"
    if len(res)>=0:
        y=Card.objects.none()
        j=0
        for i in res:
            x = Card.objects.filter(name=res[j])
            y = y | x
            j+=1
        queryset = y  
    #    print(queryset)
    else:
        queryset = Card.objects.none()

    #typical script
    serializer_class = EmenuSerializer2
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CardListAuth(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = Card.objects.all()
    serializer_class = EmenuSerializer2
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CardItemsList(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = CardItems.objects.all()
    serializer_class = EmenuSerializer3
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CardView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = Card.objects.all()
        queryset2 = CardItems.objects.all()
        queryset3 = Dish.objects.all()
        template_name = 'eMenu/cards.html'
        context = {'cards':queryset, 'cardsitems':queryset2, 'dishdata':queryset3,}
        return render(request, template_name, context)
