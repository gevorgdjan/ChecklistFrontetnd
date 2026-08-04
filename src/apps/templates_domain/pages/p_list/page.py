from django.views.generic import TemplateView

from apps.templates_domain.pages.p_list.context import get_checklist_templates_context


class ChecklistTemplateListView(TemplateView):
    """Страница со списком шаблонов чек-листов."""

    template_name = "template/pages/page_list/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_checklist_templates_context())
        return context