from polipak_sdk.base.base_api import BaseApi
from polipak_sdk.jwt_utils.actor import ActorContext


class TemplatesApi(BaseApi):
    BASE_PATH = '/api/checklist/templates'
    
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
            data=data,
        )
    
    def update(self, template_id: int, data: dict,):
        return self._client.request(
            "PUT",
            path=f"{self.BASE_PATH}/{template_id}/",
            json=data,
        )
