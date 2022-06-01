import os


def get_secret(key, default):
    try:
        with open(f'/run/secrets/{key}') as secret_file:
            return secret_file.read()
    except:
        try:
            return os.environ[key]
        except:
            return default


BASE_CANVAS_URL = get_secret(
    'BASE_CANVAS_URL', 'https://canvas.lucabergman.nl')
BASE_APP_URL = get_secret('BASE_APP_URL', 'http://localhost')
BASE_APP_API_URL = f'{BASE_APP_URL}/api/v1'
BASE_APP_API_CALLBACK_URL = f'{BASE_APP_API_URL}/auth/callback'
JWT_ALGORITHM = get_secret('JWT_ALGORITHM', 'HS256')
DATABASE_URL = get_secret('DATABASE_URL', 'db')
CLIENT_ID = get_secret('CANVAS_CLIENT_ID', '')
CLIENT_SECRET = get_secret('CANVAS_CLIENT_SECRET', '')
JWT_SECRET = get_secret('JWT_SECRET', '123')
DEVELOPER_KEY = get_secret('CANVAS_DEVELOPER_KEY', '')
DELEVOPER_KEY_ID = get_secret('CANVAS_DEVELOPER_KEY_ID', '')
POSTGRES_USER = get_secret('POSTGRES_USER', 'feeby')
POSTGRES_PASSWORD = get_secret('POSTGRES_PASSWORD', 'hallo123')
