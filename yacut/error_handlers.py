from http import HTTPStatus

from flask import jsonify, render_template
from werkzeug.exceptions import NotFound, InternalServerError

from yacut import app, db
from yacut.exceptions import InvalidAPIUsage


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage) -> tuple:
    """Возвращает ошибку в JSON формате."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error: NotFound) -> tuple:
    """Возвращает кастомную страницу 404."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error: InternalServerError) -> tuple:
    """Возвращает кастомную страницу 500."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
