from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """Модель представления соответсвия длинной ссылки к короткой."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Возвращает словарь свойств."""
        return {
            'url': self.original,
            'short_link': url_for('redirect_view', short_id=self.short, _external=True),
        }

    def from_dict(self, data):
        """Присваивает значения свойствам класса."""
        field_name = {'url': 'original', 'custom_id': 'short', }
        for field, name in field_name.items():
            if field in data:
                setattr(self, name, data[field])