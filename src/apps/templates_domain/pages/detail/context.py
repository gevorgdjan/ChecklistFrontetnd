from datetime import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_template_context(
    template_id: int,
) -> dict[str, Any]:
    """
    Возвращает контекст страницы шаблона чек-листа.

    Пока используются тестовые данные. В дальнейшем здесь будет
    выполняться запрос к API.
    """
    client = get_checklist_client()
    template = client.templates.get(template_id)
    # template = {
    #     "id": template_id,
    #     "equipment_uid": "EQ-999-XYZ",
    #     "checklist_type": "INSPECTION",
    #     "created_at": datetime.fromisoformat(
    #         "2026-08-04T08:22:04.918694+00:00",
    #     ),
    #     "fields": [
    #         {
    #             "id": 1,
    #             "name": "Температура двигателя",
    #             "field_type": "INTEGER",
    #             "order": 1,
    #             "choices": [],
    #         },
    #         {
    #             "id": 2,
    #             "name": "Внешнее состояние",
    #             "field_type": "CHOICE",
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
    #             "order": 3,
    #             "choices": [],
    #         },
    #     ],
    # }

    checklist_type_labels = {
        "INSPECTION": "Осмотр",
        "ACCEPTANCE": "Приемка",
        "HANDOVER": "Сдача",
    }

    field_type_labels = {
        "STRING": "Строка",
        "INTEGER": "Число",
        "CHOICE": "Выбор из списка",
        "CHECKBOX": "Флажок",
        "AUTO": "Автоматическое",
    }

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
        "template": template,
    }