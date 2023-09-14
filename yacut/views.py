from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from yacut import app, db
from yacut.forms import URLForm
from yacut.functions import get_unique_short_id
from yacut.models import URLMap


@app.route('/', methods=['GET', 'POST'])
def create_short_url_view():
    """Создание новой короткой ссылки."""
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id and URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!', 'custom-id-error')
            return render_template('create_short_url.html', form=form)
        if not custom_id:
            custom_id = get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('create_short_url.html', form=form, short_id=custom_id)
    return render_template('create_short_url.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    """Перенаправляет с короткой ссылки на длинную."""
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map:
        return redirect(url_map.original)
    abort(HTTPStatus.NOT_FOUND)