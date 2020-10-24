"""Todo Model."""

from config.database import Model
from orator.orm import belongs_to


class Todo(Model):
    """Todo Model."""
    __fillable__ = ["name", "description", "user_id"]

    @belongs_to("user_id", "id")
    def user(self):
        from app.User import User
        return User