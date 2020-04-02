from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('Character/<int:Characters_id>/', views.Characters_page, name='Characters_page'),

    path('Location/<int:Location_id>/', views.Location_page, name='Location_page'),

    path('Episode/<int:Episode_id>/', views.Episode_page, name='Episode_page'),

]

