import os

from dotenv import load_dotenv

from polipak_sdk.checklist.client import ChecklistClient


def get_checklist_client():
    load_dotenv()
    return ChecklistClient(
        base_url=os.environ.get(
            'SYSTEM_CHECKLIST_API_BASE_URL',
        ),
        # auth=auth,
    )
