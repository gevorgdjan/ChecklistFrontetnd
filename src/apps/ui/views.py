import time

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def get_notifications():
    time.sleep(1)
    return [
        {
            'title': 'Новая рекламация',
            'message': 'Создана рекламация CL-2026-001',
            'time': '5 минут назад',
        },
        {
            'title': 'Критический сценарий',
            'message': 'Запущен отзыв продукции',
            'time': '15 минут назад',
        },
        {
            'title': 'Контроль выполнен',
            'message': 'Корректирующие действия завершены',
            'time': '1 час назад',
        },
    ]


class NotificationsDropdownView(TemplateView):
    template_name = 'ui/components/notifications/dropdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['notifications'] = get_notifications()

        return context


MOCK_USERS = [
    {
        'id': 1,
        'name': 'Иванов',
    },
    {
        'id': 2,
        'name': 'Петров',
    },
    {
        'id': 3,
        'name': 'Сидоров',
    },
    {
        'id': 4,
        'name': 'Александров',
    },
]


class UserSelectView(View):
    template_name = 'ui/partials/user_select_dropdown.html'

    def get(self, request):

        search = (
            request.GET.get(
                'assigned_to_search',
                '',
            )
            .strip()
            .lower()
        )

        if search:
            users = [user for user in MOCK_USERS if search in user['name'].lower()]

        else:
            users = MOCK_USERS

        return render(
            request,
            self.template_name,
            {
                'users': users,
            },
        )


MOCK_PARTNERS = [
    {
        'id': 'coca_cola',
        'name': 'Coca-Cola',
    },
    {
        'id': 'pepsi',
        'name': 'Pepsi',
    },
    {
        'id': 'nestle',
        'name': 'Nestle',
    },
    {
        'id': 'danone',
        'name': 'Danone',
    },
]


class PartnerSelectView(View):
    template_name = 'ui/partials/partner_select_dropdown.html'

    def get(self, request):

        search = (
            request.GET.get(
                'partner_search',
                '',
            )
            .strip()
            .lower()
        )

        if search:
            partners = [
                partner
                for partner in MOCK_PARTNERS
                if search in partner['name'].lower()
            ]

        else:
            partners = MOCK_PARTNERS

        return render(
            request,
            self.template_name,
            {
                'partners': partners,
            },
        )


class EmptyView(TemplateView):
    template_name = 'ui/partials/empty.html'
