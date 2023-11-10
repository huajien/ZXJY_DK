import hashlib
import hmac


def encodeSha256(key, message):
    hashed = hmac.new(bytes(key, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha256)
    return hashed.hexdigest()
