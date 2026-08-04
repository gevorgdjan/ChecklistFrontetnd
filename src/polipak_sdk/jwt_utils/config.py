import os
from pathlib import Path

from dotenv import load_dotenv


def load_jwt_config():
    """Загрузка JWT настроек."""
    load_dotenv()

    private_key_path = os.environ.get('JWT_PRIVATE_KEY_PATH')
    if not private_key_path:
        raise RuntimeError('JWT_PRIVATE_KEY_PATH is not set')

    key_file = Path(private_key_path)
    if not key_file.exists():
        raise RuntimeError(f'JWT private key file not found: {key_file}')

    return {
        'private_key': key_file.read_bytes(),
        'issuer': os.environ.get('JWT_ISSUER', 'PROTOHUB-JWT'),
        'ttl': int(os.environ.get('JWT_TTL_SECONDS', '300')),
    }


# TECH_API_BASE_URL = os.environ.get('SYSTEM_TECH_API_BASE_URL')
# JWT_TECH_AUDIENCE = os.environ.get('JWT_TECH_AUDIENCE', 'TECH-API')
