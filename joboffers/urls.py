from django.urls import path
from .views import JobsListView, JobDetailView, JobCreateView

urlpatterns = [
    path('', JobsListView.as_view(), name ='joboffers_jobs'),
    path('create/', JobCreateView.as_view(), name='joboffers_create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         JobDetailView.as_view(),name ='joboffers_detail'),
]
