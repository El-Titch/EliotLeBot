#Discord Role ID
import os
from dotenv.main import load_dotenv

load_dotenv()

CLIENT_NAME = str(os.getenv("CLIENT_NAME", ""))
FOLLOWER_ROLE_ID = int(os.getenv("FOLLOWER_ROLE_ID", ''))
NOTIFS_ROLE_ID = int(os.getenv("NOTIFS_ROLE_ID", ''))
