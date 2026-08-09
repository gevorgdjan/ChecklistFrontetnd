import json
from typing import Any
from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_result_update_context(result_id: int) -> dict[str, Any]:
    client = get_checklist_client()

    result = client.results.get(result_id)

    templates = client.templates.list(
        equipment_uid=result['equipment_uid'],
        checklist_type=result['checklist_type']
    )
    if not templates:
        raise ValueError("Актуальный шаблон для этой анкеты не найден")

    template = templates[0]

    answers_dict = {}
    for ans in result.get("answers", []):
        val = ans["value"]

        field = next((f for f in template.get("fields", []) if f["id"] == ans["field_id"]), None)
        if field and field["field_type"] == "CHECKBOX":
            val = (str(val).lower() == 'true')

        answers_dict[ans["field_id"]] = val

    return {
        'result_id': result_id,
        'user_uid': result["user_uid"],
        'template_json': json.dumps(template, default=str),
        'answers_json': json.dumps(answers_dict, default=str),
    }