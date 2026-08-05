import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_result_detail_context(
        template_id: int,
) -> dict[str, Any]:
    """
    Возвращает контекст страницы анкеты чек-листа.
    """
    client = get_checklist_client()
    template = client.results.get(template_id)

    # template = {
    #     "id": template_id,
    #     "equipment_uid": "EQ-999-XYZ",
    #     "checklist_type": "INSPECTION",
    #     "checklist_type_display": "Осмотр",
    #     "created_at": datetime.datetime.fromisoformat(
    #         "2026-08-04T08:22:04.918694+00:00",
    #     ),
    #     "fields": [
    #         {
    #             "id": 1,
    #             "name": "Температура двигателя",
    #             "field_type": "INTEGER",
    #             "field_type_display": "Число",
    #             "order": 1,
    #             "choices": [],
    #         },
    #         {
    #             "id": 2,
    #             "name": "Внешнее состояние",
    #             "field_type": "CHOICE",
    #             "field_type_display": "Выбор из списка",
    #             "order": 2,
    #             "choices": [
    #                 {
    #                     "value": "Идеальное",
    #                     "order": 1,
    #                 },
    #                 {
    #                     "value": "Царапины",
    #                     "order": 2,
    #                 },
    #             ],
    #         },
    #         {
    #             "id": 3,
    #             "name": "Текущая дата осмотра",
    #             "field_type": "AUTO",
    #             "field_type_display": "Автоматическое",
    #             "order": 3,
    #             "choices": [],
    #         },
    #     ],
    # }

    return {
        'template': template,
    }