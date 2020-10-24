"""User Model."""

from config.database import Model
from orator.orm import has_many


class User(Model):
    """User Model."""

    __fillable__ = ['name', 'email', 'password']

    __auth__ = 'email'

    @has_many("user_id", "id")
    def todos(self):
        from app.Todo import Todo
        return Todo
