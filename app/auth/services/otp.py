from app.env import SECRET_KEY
import hashlib
from datetime import date
import base64


def generate_otp(username: str) -> str:
    key = f"{username}.{SECRET_KEY}.{str(date.today())}"
    otp_hash = hashlib.sha256(key.encode()).digest()
    b32 = base64.b32encode(otp_hash).decode("utf-8")
    return b32[:6].upper()


def check_otp(username: str, submitted_otp: str) -> bool:
    key = f"{username}.{SECRET_KEY}.{str(date.today())}"
    otp_hash = hashlib.sha256(key.encode()).digest()
    b32 = base64.b32encode(otp_hash).decode("utf-8")
    expected_otp = b32[:6].upper()
    return submitted_otp == expected_otp
