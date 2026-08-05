import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_result_detail_context(result_id: int) -> dict[str, Any]:
    """
    Возвращает контекст для детальной страницы заполненного чек-листа.
    """
    # --- РАБОЧИЙ ВАРИАНТ ---
    client = get_checklist_client()
    result = client.results.get(result_id)

    # # --- ЗАГЛУШКА ---
    # result = {
    #     "id": result_id,
    #     "equipment_uid": "EQ-FORKLIFT-01",
    #     "user_uid": "USER-DRIVER-007",
    #     "checklist_type": "INSPECTION",
    #     "checklist_type_display": "Осмотр",
    #     # Имитируем, что API вернуло СТРОКУ, а не объект (как в реальности)
    #     "created_at": "2026-08-05T08:15:00Z",
    #     "answers": [
    #         {
    #             "field_id": 1,
    #             "field_name": "Давление в шинах",
    #             "field_type": "NUMBER",
    #             "field_type_display": "Число",
    #             "value": "7"
    #         },
    #         {
    #             "field_id": 2,
    #             "field_name": "Состояние",
    #             "field_type": "CHOICE",
    #             "field_type_display": "Выбор из списка",
    #             "value": "В норме"
    #         },
    #         {
    #             "field_id": 3,
    #             "field_name": "Сигналка работает?",
    #             "field_type": "CHECKBOX",
    #             "field_type_display": "Чекбокс",
    #             "value": "true"
    #         }
    #     ]
    # }

    if isinstance(result.get('created_at'), str):
        date_str = result['created_at'].replace('Z', '+00:00')
        result['created_at'] = datetime.datetime.fromisoformat(date_str)

    return {
        'result': result,
    }