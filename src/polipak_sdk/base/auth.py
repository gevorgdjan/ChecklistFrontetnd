class BaseAuth:
    """Базовая стратегия авторизации."""

    def build_headers(self, actor=None) -> dict:
        """Построить auth headers."""
        return {}
