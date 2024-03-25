from django.shortcuts import render
from .models import *
from django.views import generic
from django.urls import reverse_lazy

class VacancyListView(generic.ListView):
    model = Vacancy
    template_name = 'home.html'

class VacancyDetailView(generic.DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'
    

class ApplicationsCreateView(generic.CreateView):
    model = Applications
    template_name = 'create_app.html'
    fields = '__all__'
    success_url = reverse_lazy('vacancy_list')    
