from django.views.generic import TemplateView, ListView

from joboffers.models import JobOffer


class HomePageView(ListView):
    template_name = 'home.html'
    model = JobOffer
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return JobOffer.published.all().order_by('-publish')

class AboutPageView(TemplateView):
    template_name = 'about.html'
