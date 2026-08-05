from django.urls import path

from apps.results_domain.pages.create.page import ChecklistResultCreateView
from apps.results_domain.pages.p_list.page import ChecklistResultsListView
from apps.results_domain.pages.delete.page import ChecklistResultDeleteView
from apps.results_domain.pages.details.page import ChecklistResultDetailView
from apps.results_domain.pages.update.page import ChecklistResultUpdateView


app_name = 'results_domain'

urlpatterns = [
    path(
        'results/',
        ChecklistResultsListView.as_view(),
        name='result-list',
    ),
    path(
        'results/create/',
        ChecklistResultCreateView.as_view(),
        name='result-create'
    ),
    path(
        '<int:pk>/',
        ChecklistResultDetailView.as_view(),
        name='result-detail'
    ),
    path(
        '<int:pk>/update/',
        ChecklistResultUpdateView.as_view(),
        name='result-update'
    ),
    path(
        '<int:pk>/delete/',
        ChecklistResultDeleteView.as_view(),
        name='result-delete'
    ),
]
