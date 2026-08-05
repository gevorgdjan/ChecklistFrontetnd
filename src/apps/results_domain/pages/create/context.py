import json
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_form_context(equipment_uid: str, checklist_type: str) -> dict[str, Any]:
    """
    Запрашивает пустой бланк шаблона для заполнения.
    """

    client = get_checklist_client()
    template = client.templates.list(equipment_uid=equipment_uid, checklist_type=checklist_type)[0]

    # template = {
    #     "id": 1,
    #     "equipment_uid": equipment_uid,
    #     "checklist_type": checklist_type,
    #     "checklist_type_display": "Осмотр" if checklist_type == "INSPECTION" else "Приемка",
    #     "fields": [
    #         {
    #             "id": 10,
    #             "name": "Давление в шинах (Атм)",
    #             "field_type": "NUMBER",
    #             "field_type_display": "Число",
    #             "choices": []
    #         },
    #         {
    #             "id": 11,
    #             "name": "Внешнее состояние",
    #             "field_type": "CHOICE",
    #             "field_type_display": "Выбор из списка",
    #             "choices": [{"value": "Идеальное"}, {"value": "Царапины"}]
    #         },
    #         {
    #             "id": 12,
    #             "name": "Двигатель заводится?",
    #             "field_type": "CHECKBOX",
    #             "field_type_display": "Чекбокс",
    #             "choices": []
    #         },
    #         {
    #             "id": 13,
    #             "name": "Дата и время",
    #             "field_type": "AUTO",
    #             "field_type_display": "Автозаполнение",
    #             "choices": []
    #         }
    #     ]
    # }

    return {
        'template': template,
        'template_json': json.dumps(template)
    }