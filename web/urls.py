from django.urls import path
from .views import *
urlpatterns = [
  path('',VacancyListView.as_view(),name='vacancy_list'),
  path('more_info/<int:pk>/',VacancyDetailView.as_view(),name='more_info'),
  path('create_app/<int:pk>/',ApplicationsCreateView.as_view(),name='create_app')
]
