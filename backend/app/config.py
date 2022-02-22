import os

CLIENT_ID = os.environ.get("LTI_CONSUMER_KEY")
CLIENT_SECRET = os.environ.get("LTI_SHARED_SECRET")

# Canvas instance
BASE_URL = os.environ.get("BASE_URL")

# Hosted LTI instance
BASE_APP_URL = os.environ.get("BASE_APP_URL")
BASE_APP_API_URL = BASE_APP_URL + '/api/v1' # make /api/v1 also an env. var. so it can be set to /api/v2 if ever needed