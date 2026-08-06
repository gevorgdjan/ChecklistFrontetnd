
from polipak_sdk.base.base_api import BaseApi


class ResultsApi(BaseApi):
    BASE_PATH = '/api/v1/results'

    def list(self, equipment_uid: str = None, user_uid: str = None):
        """Получить историю анкет с фильтрацией"""
        params = {}
        if equipment_uid: params['equipment_uid'] = equipment_uid
        if user_uid: params['user_uid'] = user_uid

        return self._client.request('GET', path=f'{self.BASE_PATH}/',
                                    params=params)

    def get(self, result_id: int):
        return self._client.request('GET',
                                    path=f'{self.BASE_PATH}/{result_id}/')

    def create(self, data: dict):
        return self._client.request('POST', path=f'{self.BASE_PATH}/',
                                    json=data)

    def update(
        self,
        result_id: int,
        data: dict,
    ):
        return self._client.request(
            'PUT',
            path=f'{self.BASE_PATH}/{result_id}/',
            json=data,
        )

    def delete(self, result_id: int):
        """
        Отправляет DELETE запрос в REST API для удаления анкеты.
        """
        return self._client.request(
            'DELETE',
            path=f'{self.BASE_PATH}/{result_id}/',
        )
