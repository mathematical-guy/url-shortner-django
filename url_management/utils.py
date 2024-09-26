import string
import random


def shortend_url_object_id_generator(prefix=None, length=8) -> str:
    POSSIBLE_CHARACTERS: str = string.ascii_letters + string.digits
    return ''.join([random.choice(POSSIBLE_CHARACTERS) for _ in range(length)])
