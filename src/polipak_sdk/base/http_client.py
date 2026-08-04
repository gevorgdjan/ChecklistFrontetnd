import logging
from typing import TYPE_CHECKING, Union

import requests

if TYPE_CHECKING:
    from polipak_sdk.base.auth import BaseAuth

logger = logging.getLogger(__name__)


class HttpClient:
    """Клиент HTTP."""

    def __init__(
        self,
        *,
        base_url: str,
        auth: Union['BaseAuth', None] = None,
        timeout: float = 10,
    ):
        """Инициализация."""
        self._base_url = base_url.rstrip('/')
        self._session = requests.Session()
        self._auth = auth
        self._default_timeout = timeout

    def _build_headers(self, actor=None, headers=None):
        """Собрать headers."""

        return {
            **(headers or {}),
            **(self._auth.build_headers(actor) if self._auth else {}),
        }

    def _request(
        self,
        method: str,
        *,
        path: str,
        actor=None,
        timeout: float | None = None,
        **kwargs,
    ):
        """Базовый HTTP-запрос."""
        return self._session.request(
            method=method,
            url=f'{self._base_url}/{path.lstrip("/")}',
            headers=self._build_headers(actor),
            timeout=timeout or self._default_timeout,
            **kwargs,
        )

    def request(
        self,
        method: str,
        *,
        path: str,
        actor=None,
        params=None,
        data=None,
        json=None,
        headers=None,
        files=None,
        timeout=None,
    ):
        """Универсальный запрос (для proxy/gateway)."""

        response = self._session.request(
            method=method,
            url=f'{self._base_url}/{path.lstrip("/")}',
            headers={
                **(headers or {}),
                **self._build_headers(actor),
            },
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=timeout or self._default_timeout,
        )
        try:
            response.raise_for_status()
        except Exception:
            logger.error(response.text)
            raise
        if not response.content:
            return None

        return response.json()
