import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_templates_context(equipment_uid: str | None = None, checklist_type: str | None = None) -> dict[
    str, Any]:
    client = get_checklist_client()
    templates = client.templates.list(equipment_uid=equipment_uid, checklist_type=checklist_type)

    equipment_list = client.templates.get_equipments()

    for t in templates:
        if isinstance(t.get('created_at'), str):
            t['created_at'] = datetime.datetime.fromisoformat(t['created_at'].replace('Z', '+00:00'))

    return {
        'templates': templates,
        'equipment_list': equipment_list,  # <-- ПЕРЕДАЕМ В ШАБЛОН
    }