import os


def get_secret_from_file(path):
    with open(path) as secret_file:
        return secret_file.read()


try:
    BASE_CANVAS_URL = os.environ['BASE_CANVAS_URL']
    BASE_APP_URL = os.environ['BASE_APP_URL']
    BASE_APP_API_URL = f'{BASE_APP_URL}/api/v1'
    BASE_APP_API_CALLBACK_URL = f'{BASE_APP_API_URL}/auth/callback'
    JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
    DATABASE_URL = os.environ['DATABASE_URL']
    CLIENT_ID = get_secret_from_file(os.environ['CANVAS_CLIENT_ID_FILE'])
    CLIENT_SECRET = get_secret_from_file(
        os.environ['CANVAS_CLIENT_SECRET_FILE'])
    JWT_SECRET = get_secret_from_file(os.environ['JWT_SECRET_FILE'])
    DEVELOPER_KEY = get_secret_from_file(
        os.environ['CANVAS_DEVELOPER_KEY_FILE'])
    DELEVOPER_KEY_ID = get_secret_from_file(
        os.environ['CANVAS_DEVELOPER_KEY_ID_FILE'])
    POSTGRES_USER = get_secret_from_file(os.environ['POSTGRES_USER_FILE'])
    POSTGRES_PASSWORD = get_secret_from_file(
        os.environ['POSTGRES_PASSWORD_FILE'])
except KeyError as err:
    print(f"Given key not found - {err}")
