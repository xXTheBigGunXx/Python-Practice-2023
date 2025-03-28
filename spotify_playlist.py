from dotenv import load_dotenv
import os
import base64

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

def get_toke():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"