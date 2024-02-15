import bcrypt


def generate_salt() -> bytes:
    return bcrypt.gensalt()


def hash_password(password: str, salt: bytes):
    bytePassword: bytes = password.encode('utf-8')
    return bcrypt.hashpw(bytePassword, salt)
