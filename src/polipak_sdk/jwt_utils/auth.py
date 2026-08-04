from polipak_sdk.base.auth import BaseAuth


class JwtAuth(BaseAuth):
    """JWT авторизация."""

    def __init__(self, token_factory):
        self._token_factory = token_factory

    def build_headers(self, actor=None) -> dict:
        """Построить JWT headers."""

        if actor is None:
            return {}

        token = self._token_factory.create(actor)

        return {
            'Authorization': f'Bearer {token}',
        }
