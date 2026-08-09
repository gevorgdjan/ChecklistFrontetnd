import json
from typing import Any
from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_form_context(equipment_uid: str, checklist_type: str) -> dict[str, Any]:
    client = get_checklist_client()

    response_data = client.templates.list(equipment_uid=equipment_uid, checklist_type=checklist_type)

    print(f"[DEBUG SDK] Ответ от API: {response_data}")

    if isinstance(response_data, dict) and 'results' in response_data:
        templates_list = response_data['results']
    elif isinstance(response_data, list):
        templates_list = response_data
    else:
        templates_list = []

    if not templates_list:
        raise ValueError(f"Шаблон не найден для {equipment_uid} ({checklist_type})")

    template = templates_list[0]

    return {
        'checklist_template': template,
        'checklist_template_json': json.dumps(template, default=str)
    }