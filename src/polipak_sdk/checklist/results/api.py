from polipak_sdk.base.base_api import BaseApi
from polipak_sdk.jwt_utils.actor import ActorContext


class TemplatesApi(BaseApi):
    BASE_PATH = '/api/checklist'

    # def short_tree(self, serial: str):
    #     return self._client.request(
    #         'GET', path=self.BASE_PATH + '/' + serial, actor=ActorContext(type='system')
    #     )

    # def product_info(self, serial: str):
    #     response = self._client.request(
    #         'GET',
    #         path='/api/v1/track/tree/',
    #         params={
    #             'serial': serial,
    #             'direction': 'from_product',
    #         },
    #         actor=ActorContext(type='system'),
    #     )
    #
    #     return response
