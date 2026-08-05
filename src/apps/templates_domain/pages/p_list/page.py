from django.views.generic import TemplateView

from apps.templates_domain.pages.p_list.context import get_checklist_templates_context


class ChecklistTemplateListView(TemplateView):
    """Страница со списком шаблонов чек-листов."""

    template_name = 'templates_domain/pages/page_list/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        equipment_uid = self.request.GET.get('equipment_uid')
        checklist_type = self.request.GET.get('checklist_type')

        context.update(
            get_checklist_templates_context(equipment_uid, checklist_type))
        return context
