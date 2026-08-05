from polipak_sdk.base.http_client import HttpClient
from polipak_sdk.checklist.templates.api import TemplatesApi

from polipak_sdk.checklist.results.api import ResultsApi


class ChecklistClient(HttpClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.templates = TemplatesApi(self)
        self.results = ResultsApi(self)
