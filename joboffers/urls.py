from django.urls import path
from .views import JobsListView, JobDetailView

urlpatterns = [
    path('', JobsListView.as_view(), name ='list'),
]
