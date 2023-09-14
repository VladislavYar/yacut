from http import HTTPStatus
import re

from flask import jsonify, request

from yacut import app, db
from yacut.exceptions import InvalidAPIUsage
from yacut.models import URLMap
from yacut.functions import get_unique_short_id
from yacut.constants import REG_VALIATION_SHORT_ID, MAX_LEN_SHORT_ID


def validate_create_short_url(data):
    """Валидирует данные при создании короткой ссылки."""
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)

    custom_id = data.get('custom_id')
    if not data.get('url'):
        raise InvalidAPIUsage('"url" является обязательным полем!', HTTPStatus.BAD_REQUEST)
    if custom_id:
        if len(custom_id) > MAX_LEN_SHORT_ID or not re.match(REG_VALIATION_SHORT_ID, custom_id):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки',
                                  HTTPStatus.BAD_REQUEST)
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.',
                                  HTTPStatus.BAD_REQUEST)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Отдаёт длинный URL."""
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    """Создает новую короткую ссылку."""
    data = request.get_json()
    validate_create_short_url(data)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()

    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
