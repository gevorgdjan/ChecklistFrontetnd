from typing import Any
from polipak_sdk.checklist.factories import get_checklist_client
import datetime

def get_checklist_template_context(template_id: int) -> dict[str, Any]:
    client = get_checklist_client()
    template = client.templates.get(template_id)

    for date_field in ['created_at', 'updated_at']:
        if isinstance(template.get(date_field), str):
            template[date_field] = datetime.datetime.fromisoformat(template[date_field].replace('Z', '+00:00'))

    return {'template': template}