import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client

def get_checklist_results_context(
        equipment_uid: str | None = None,
        user_uid: str | None = None
) -> dict[str, Any]:
    """
    Формирует контекст страницы со списком заполненных чек-листов (результатов).
    """

    client = get_checklist_client()
    results = client.results.list(
        equipment_uid=equipment_uid,
        user_uid=user_uid
    )

    # results = [
    #     {
    #         "id": 1,
    #         "equipment_uid": "EQ-FORKLIFT-01",
    #         "user_uid": "USER-DRIVER-007",
    #         "checklist_type": "INSPECTION",
    #         "checklist_type_display": "Осмотр",
    #         "created_at": datetime.datetime.fromisoformat("2026-08-05T08:15:00+00:00"),
    #         "answers": [
    #             {
    #                 "field_id": 1,
    #                 "field_name": "Давление в шинах",
    #                 "field_type": "NUMBER",
    #                 "field_type_display": "Число",
    #                 "value": "7"
    #             },
    #             {
    #                 "field_id": 2,
    #                 "field_name": "Состояние",
    #                 "field_type": "CHOICE",
    #                 "field_type_display": "Выбор из списка",
    #                 "value": "В норме"
    #             }
    #         ]
    #     },
    #     {
    #         "id": 2,
    #         "equipment_uid": "EQ-MACBOOK-99",
    #         "user_uid": "USER-IT-001",
    #         "checklist_type": "HANDOVER",
    #         "checklist_type_display": "Сдача",
    #         "created_at": datetime.datetime.fromisoformat("2026-08-04T16:30:00+00:00"),
    #         "answers": [
    #             {
    #                 "field_id": 3,
    #                 "field_name": "ФИО Сотрудника",
    #                 "field_type": "TEXT",
    #                 "field_type_display": "Строка",
    #                 "value": "Иванов И.И."
    #             }
    #         ]
    #     }
    # ]

    return {
        'results': results,
    }