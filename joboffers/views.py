from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, \
    UpdateView, DeleteView

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
        context['form'] = JobForm()
        return context


class JobDetailView(DetailView, LoginRequiredMixin):
    model = JobOffer
    template_name = 'jobs/detail.html'
    context_object_name = 'job'
    exclude = ('uuid', 'slug', 'author')


class JobCreateView(CreateView, LoginRequiredMixin):
    form_class = JobForm
    template_name = 'jobs/create.html'
    model = JobOffer

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('joboffers_jobs')


class JobUpdateView(JobCreateView, UpdateView):
    template_name = 'jobs/update.html'

class JobDeleteView(JobDetailView, DeleteView):
    template_name = 'jobs/delete.html'


class PublishedView(ListView):
    model = JobOffer
    template_name = 'jobs/published.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return JobOffer.published.all().filter().order_by('-publish')

