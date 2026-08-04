from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class ActorContext:
    """Контекст актора."""

    type: Literal['human', 'system']
    user_id: str | None = None
