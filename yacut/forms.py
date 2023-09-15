from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Regexp

from yacut.constants import MAX_LEN_SHORT_ID, REG_VALIATION_SHORT_ID


class URLForm(FlaskForm):
    """Форма добавления нового соответсвия длинной ссылки к короткой."""
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                max=MAX_LEN_SHORT_ID,
                message=('Длина должна быть не больше '
                         f'{MAX_LEN_SHORT_ID} символов')),
            Regexp(REG_VALIATION_SHORT_ID,
                   message='Допустимы только символы A-z и 0-9')
        ]
    )
    submit = SubmitField('Создать')
