import os
from dotenv import load_dotenv

load_dotenv()


CLIENT_ID = os.environ["LTI_CONSUMER_KEY"]
CLIENT_SECRET = os.environ["LTI_SHARED_SECRET"]
DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]

# Canvas instance
BASE_URL = os.environ["BASE_URL"]

# Hosted LTI instance
BASE_APP_URL = os.environ["BASE_APP_URL"]
BASE_APP_API_URL = f'{BASE_APP_URL}' # make /api/v1 dynamic so it can be set to something else

