from random import choices
from string import ascii_letters, digits

from yacut.constants import DEFAULT_LEN_SHORT_ID
from yacut.models import URLMap


def get_unique_short_id():
    """Создаёт уникальный id."""
    while True:
        short_id = ''.join(choices(ascii_letters + digits, k=DEFAULT_LEN_SHORT_ID))
        if URLMap.query.filter_by(short=short_id).first():
            continue
        return short_id