from django.views.generic import TemplateView

from apps.templates_domain.pages.detail.context import get_checklist_template_context


class ChecklistTemplateDetailView(TemplateView):
    template_name = "templates_domain/pages/detail/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            get_checklist_template_context(self.kwargs["pk"])
        )
        return context