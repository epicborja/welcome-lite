from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobOffer

class JobsListView(ListView):
    model = JobOffer
    template_name = 'jobs/list.html'

class JobDetailView(DetailView):
    model = JobOffer
    template_name = 'jobs/detail.html'
