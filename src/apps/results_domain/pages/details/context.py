import datetime
from typing import Any

from polipak_sdk.checklist.factories import get_checklist_client


def get_checklist_result_detail_context(result_id: int) -> dict[str, Any]:
    client = get_checklist_client()
    result = client.results.get(result_id)

    for date_field in ['created_at', 'updated_at']:
        if isinstance(result.get(date_field), str):
            result[date_field] = datetime.datetime.fromisoformat(result[date_field].replace('Z', '+00:00'))

    return {'result': result}
