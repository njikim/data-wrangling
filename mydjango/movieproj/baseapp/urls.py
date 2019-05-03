from django.urls import path
from baseapp import views
 
urlpatterns = [
    path('', views.home),
    path('genre', views.genre),
    path('genre/result', views.genre_result),

]