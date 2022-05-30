import os


def get_secret_from_file(path):
    with open(f'/run/secrets/{path}') as secret_file:
        return secret_file.read()


try:
    BASE_CANVAS_URL = os.environ['BASE_CANVAS_URL']
    BASE_APP_URL = os.environ['BASE_APP_URL']
    BASE_APP_API_URL = f'{BASE_APP_URL}/api/v1'
    BASE_APP_API_CALLBACK_URL = f'{BASE_APP_API_URL}/auth/callback'
    JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
    DATABASE_URL = os.environ['DATABASE_URL']
    try:
        CLIENT_ID = get_secret_from_file('CANVAS_CLIENT_ID')
        CLIENT_SECRET = get_secret_from_file('CANVAS_CLIENT_SECRET')
        JWT_SECRET = get_secret_from_file('JWT_SECRET')
        DEVELOPER_KEY = get_secret_from_file('CANVAS_DEVELOPER_KEY')
        DELEVOPER_KEY_ID = get_secret_from_file('CANVAS_DEVELOPER_KEY_ID')
        POSTGRES_USER = get_secret_from_file('POSTGRES_USER')
        POSTGRES_PASSWORD = get_secret_from_file('POSTGRES_PASSWORD')
    except:
        CLIENT_ID = os.environ['CANVAS_CLIENT_ID']
        CLIENT_SECRET = os.environ['CANVAS_CLIENT_SECRET']
        JWT_SECRET = os.environ['JWT_SECRET']
        DEVELOPER_KEY = os.environ['CANVAS_DEVELOPER_KEY']
        DELEVOPER_KEY_ID = os.environ['CANVAS_DEVELOPER_KEY_ID']
        POSTGRES_USER = os.environ['POSTGRES_USER']
        POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
except KeyError as err:
    print(f"Given key not found - {err}")
