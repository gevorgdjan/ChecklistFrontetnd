from django.urls import path

from apps.templates_domain.pages.detail.page import ChecklistTemplateDetailView
from apps.templates_domain.pages.p_list.page import ChecklistTemplateListView
from apps.templates_domain.pages.update.page import ChecklistTemplateUpdateView

# TODO: распилить на несколько файлов.
app_name = 'templates_domain'
urlpatterns = [
    path(
        "templates/",
        ChecklistTemplateListView.as_view(),
        name="template-list",
    ),
    path(
        "templates/<int:pk>/",
        ChecklistTemplateDetailView.as_view(),
        name="template-detail",
    ),
    path(
        "templates/<int:pk>/edit/",
        ChecklistTemplateUpdateView.as_view(),
        name="template-update",
    ),
]
