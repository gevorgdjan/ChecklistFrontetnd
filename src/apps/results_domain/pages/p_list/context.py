import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_results_context(equipment_uid: str | None = None, user_uid: str | None = None) -> dict[str, Any]:
    client = get_checklist_client()
    results = client.results.list(equipment_uid=equipment_uid, user_uid=user_uid)

    equipment_list = client.templates.get_equipments()

    for r in results:
        val = r.get('created_at')
        if isinstance(val, str):
            r['created_at'] = datetime.datetime.fromisoformat(val.replace('Z', '+00:00'))

    return {
        'results': results,
        'equipment_list': equipment_list,  # <-- ПЕРЕДАЕМ В ШАБЛОН
    }