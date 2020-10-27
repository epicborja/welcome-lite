from django.urls import path
from .views import JobsListView, JobDetailView, JobCreateView, PublishedView, \
    JobUpdateView, JobDeleteView

urlpatterns = [
    path('', JobsListView.as_view(), name ='joboffers_jobs'),
    path('create/', JobCreateView.as_view(), name='joboffers_create'),
    path('offers/', PublishedView.as_view(), name='joboffers_published'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         JobDetailView.as_view(),name ='joboffers_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/',
         JobUpdateView.as_view(), name='joboffers_update'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/',
             JobDeleteView.as_view(), name='joboffers_delete'),
]
