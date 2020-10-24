"""A todosController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Todo import Todo

class TodosController(Controller):
    """TodosController Controller Class."""

    def __init__(self, request: Request):
        """TodosController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        todos = Todo.all()
        return view.render("todos.html", {"name": "Craig Derington", "todos": todos})


    def single(self, view: View, request: Request):
        param = self.request.id
        todo = Todo.find(param)
        return view.render(
            "todo.html",
            {"todo": todo}
        )
