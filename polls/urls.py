from django.urls import path

from . import views
from . import language
from . import system
from . import IDE

urlpatterns = [
    path('', views.index, name='index'),
    path('language/', language.indexOne, name='indexOne'),
    path('system/', system.indexThree, name='indexThree'),
    path('IDE/', IDE.indexTwo, name='indexTwo')
]