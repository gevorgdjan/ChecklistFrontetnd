from django.urls import path

from apps.templates_domain.pages.delete.page import ChecklistTemplateDeleteView
from apps.templates_domain.pages.detail.page import ChecklistTemplateDetailView
from apps.templates_domain.pages.p_list.page import ChecklistTemplateListView
from apps.templates_domain.pages.update.page import ChecklistTemplateUpdateView

from apps.templates_domain.pages.create.page import ChecklistTemplateCreateView

app_name = 'templates_domain'

urlpatterns = [
    path(
        'templates/',
        ChecklistTemplateListView.as_view(),
        name='template-list',
    ),
    path(
        'templates/create/',
        ChecklistTemplateCreateView.as_view(),
        name='template-create'
    ),
    path(
        'templates/<int:pk>/',
        ChecklistTemplateDetailView.as_view(),
        name='template-detail',
    ),
    path(
        'templates/<int:pk>/edit/',
        ChecklistTemplateUpdateView.as_view(),
        name='template-update',
    ),
    path(
        '<int:pk>/delete/',
        ChecklistTemplateDeleteView.as_view(),
        name='template-delete'),
]
