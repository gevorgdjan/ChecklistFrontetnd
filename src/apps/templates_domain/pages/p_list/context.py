from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_templates_context() -> dict[str, Any]:
    """
    Формирует контекст страницы со списком шаблонов чек-листов.

    Пока возвращает тестовые данные. В дальнейшем здесь можно получить
    шаблоны через ORM или внешний API.
    """
    client = get_checklist_client()
    templates = client.templates.list()
    
    # templates = [
    #     {
    #         "id": 1,
    #         "equipment_uid": "machine-001",
    #         "checklist_type": "INSPECTION",
    #         "created_at": "2026-08-04T08:03:32.983Z",
    #         "fields": [
    #             {
    #                 "id": 1,
    #                 "name": "Состояние корпуса",
    #                 "field_type": "STRING",
    #                 "order": 1,
    #                 "choices": [],
    #             },
    #             {
    #                 "id": 2,
    #                 "name": "Оборудование исправно",
    #                 "field_type": "CHECKBOX",
    #                 "order": 2,
    #                 "choices": [],
    #             },
    #         ],
    #     },
    #     {
    #         "id": 2,
    #         "equipment_uid": "machine-002",
    #         "checklist_type": "ACCEPTANCE",
    #         "created_at": "2026-08-03T12:30:00.000Z",
    #         "fields": [
    #             {
    #                 "id": 3,
    #                 "name": "Общее состояние",
    #                 "field_type": "CHOICE",
    #                 "order": 1,
    #                 "choices": [
    #                     {
    #                         "value": "Хорошее",
    #                         "order": 1,
    #                     },
    #                     {
    #                         "value": "Удовлетворительное",
    #                         "order": 2,
    #                     },
    #                     {
    #                         "value": "Требует ремонта",
    #                         "order": 3,
    #                     },
    #                 ],
    #             },
    #         ],
    #     },
    # ]
    
    
    checklist_type_labels = {
        "INSPECTION": "Осмотр",
        "ACCEPTANCE": "Приёмка",
        "HANDOVER": "Сдача",
    }
    
    field_type_labels = {
        "STRING": "Строка",
        "INTEGER": "Число",
        "CHOICE": "Выбор из списка",
        "CHECKBOX": "Флажок",
    }

    for template in templates:
        template["checklist_type_label"] = checklist_type_labels.get(
            template["checklist_type"],
            template["checklist_type"],
        )

        for field in template["fields"]:
            field["field_type_label"] = field_type_labels.get(
                field["field_type"],
                field["field_type"],
            )

    return {
        "templates": templates,
    }