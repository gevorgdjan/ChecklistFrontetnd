from polipak_sdk.base.http_client import HttpClient
from polipak_sdk.checklist.templates.api import TemplatesApi


class ChecklistClient(HttpClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.templates = TemplatesApi(self)
        # self.results = TemplatesApi(self)
