
from polipak_sdk.base.base_api import BaseApi


class TemplatesApi(BaseApi):
    BASE_PATH = '/api/v1/templates'

    def list(self):
        return self._client.request(
            'GET',
            path=self.BASE_PATH + '/',
        )

    def get(self, template_id):
        return self._client.request(
            'GET',
            path=self.BASE_PATH + '/' + str(template_id) + '/',
        )

    def create(self, data):

        return self._client.request(
            'POST',
            path=self.BASE_PATH + '/',
            json=data,
        )

    def update(
        self,
        template_id: int,
        data: dict,
    ):
        return self._client.request(
            'PUT',
            path=f'{self.BASE_PATH}/{template_id}/',
            json=data,
        )

    def delete(self, template_id: int):
        return self._client.request(
            'DELETE',
            path=f'{self.BASE_PATH}/{template_id}/',
        )