import json
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_result_update_context(result_id: int) -> dict[str, Any]:
    """
    Получает данные заполненной анкеты и ее шаблона для редактирования.
    """

    # --- РАБОЧИЙ ВАРИАНТ ---
    client = get_checklist_client()
    result = client.results.get(result_id)
    template = client.templates.list(
        equipment_uid=result['equipment_uid'],
        checklist_type=result['checklist_type']
    )[0]

    # --- ЗАГЛУШКА ---
    # template = {
    #     "id": 1,
    #     "equipment_uid": "EQ-FORKLIFT-01",
    #     "checklist_type": "INSPECTION",
    #     "checklist_type_display": "Осмотр",
    #     "fields": [
    #         {"id": 10, "name": "Давление в шинах (Атм)", "field_type": "NUMBER", "field_type_display": "Число",
    #          "choices": []},
    #         {"id": 11, "name": "Внешнее состояние", "field_type": "CHOICE", "field_type_display": "Выбор из списка",
    #          "choices": [{"value": "Идеальное"}, {"value": "Царапины"}]},
    #         {"id": 12, "name": "Сигналка работает?", "field_type": "CHECKBOX", "field_type_display": "Чекбокс",
    #          "choices": []},
    #         {"id": 13, "name": "Дата и время", "field_type": "AUTO", "field_type_display": "Автозаполнение",
    #          "choices": []}
    #     ]
    # }
    #
    # result = {
    #     "id": result_id,
    #     "equipment_uid": "EQ-FORKLIFT-01",
    #     "user_uid": "USER-DRIVER-007",
    #     "checklist_type": "INSPECTION",
    #     "answers": [
    #         {"field_id": 10, "value": "7"},
    #         {"field_id": 11, "value": "Царапины"},
    #         {"field_id": 12, "value": "true"},
    #         {"field_id": 13, "value": "2026-08-05 10:00:00"}
    #     ]
    # }

    answers_dict = {}
    for ans in result["answers"]:
        val = ans["value"]

        field = next((f for f in template["fields"] if f["id"] == ans["field_id"]), None)
        if field and field["field_type"] == "CHECKBOX":
            val = (str(val).lower() == 'true')

        answers_dict[ans["field_id"]] = val

    return {
        'result_id': result_id,
        'user_uid': result["user_uid"],
        'template_json': json.dumps(template),
        'answers_json': json.dumps(answers_dict),
    }