import time
from typing import TYPE_CHECKING

import jwt

if TYPE_CHECKING:
    from polipak_sdk.jwt_utils.actor import ActorContext


class TokenFactory:
    """Фабрика токенов."""

    _issuer: str
    _audience: str
    _private_key: str
    _ttl: int

    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        private_key: str,
        ttl_seconds: int,
    ):
        """Инициализация."""
        self._issuer = issuer
        self._audience = audience
        self._private_key = private_key
        self._ttl = ttl_seconds

    def human(self, user_id: str) -> str:
        """Токен пользователя."""
        payload = {
            'iss': self._issuer,
            'aud': self._audience,
            'actor_type': 'human',
            'sub': user_id,
            'exp': int(time.time()) + self._ttl,
        }
        return jwt.encode(payload, self._private_key, algorithm='RS256')

    def system(self) -> str:
        """Токен системы."""
        payload = {
            'iss': self._issuer,
            'aud': self._audience,
            'actor_type': 'system',
            'exp': int(time.time()) + self._ttl,
        }
        return jwt.encode(payload, self._private_key, algorithm='RS256')

    def create(self, actor: 'ActorContext') -> str:
        """Создание."""
        if actor.type == 'human':
            if not actor.user_id:
                raise ValueError('user_id required for human actor')
            return self.human(actor.user_id)

        return self.system()
