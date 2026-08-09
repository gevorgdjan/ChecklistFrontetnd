
from polipak_sdk.base.base_api import BaseApi


class TemplatesApi(BaseApi):
    BASE_PATH = '/api/v1/templates'

    def list(self, equipment_uid: str = None, checklist_type: str = None):
        params = {}
        if equipment_uid: params['equipment_uid'] = equipment_uid
        if checklist_type: params['checklist_type'] = checklist_type
        return self._client.request('GET', path=f'{self.BASE_PATH}/', params=params)

    def get(self, template_id: int):
        return self._client.request('GET', path=f'{self.BASE_PATH}/{template_id}/')

    def create(self, data: dict):
        return self._client.request('POST', path=f'{self.BASE_PATH}/', json=data)

    def update(self, template_id: int, data: dict):
        return self._client.request('PUT', path=f'{self.BASE_PATH}/{template_id}/', json=data)

    def delete(self, template_id: int):
        return self._client.request('DELETE', path=f'{self.BASE_PATH}/{template_id}/')

    def history(self, template_id: int):
        return self._client.request('GET', path=f'{self.BASE_PATH}/{template_id}/history/')

    def get_equipments(self):
        return self._client.request('GET', path=f'{self.BASE_PATH}/equipments/')
