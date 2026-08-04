from django.urls import path

from apps.ui.views import NotificationsDropdownView

urlpatterns = [
    path(
        'notifications/',
        NotificationsDropdownView.as_view(),
        name='notifications-dropdown',
    ),
]
