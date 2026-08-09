import datetime
from typing import Any
from polipak_sdk.checklist.factories import get_checklist_client


def get_template_history_context(template_id: int) -> dict[str, Any]:
    client = get_checklist_client()

    history = client.templates.history(template_id=template_id)

    for t in history:
        for date_field in ['created_at', 'updated_at']:
            val = t.get(date_field)
            if isinstance(val, str):
                t[date_field] = datetime.datetime.fromisoformat(val.replace('Z', '+00:00'))

    return {
        'history': history,
        'current_id': template_id
    }