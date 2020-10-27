from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .forms import JobForm
from .models import JobOffer


class JobsListView(ListView, LoginRequiredMixin):

    model = JobOffer
    template_name = 'jobs/list.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return JobOffer.objects.all().filter(
            author_id=self.request.user.id
        ).order_by('-publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JobForm(initial={'author': self.request.user})
        return context


class JobDetailView(DetailView, LoginRequiredMixin):
    model = JobOffer
    template_name = 'jobs/detail.html'
    context_object_name = 'job'


class JobCreateView(FormView, LoginRequiredMixin):
    form_class = JobForm
    template_name = 'jobs/create.html'
    model = JobOffer

    def get_success_url(self):
        return reverse_lazy('joboffers_jobs')


