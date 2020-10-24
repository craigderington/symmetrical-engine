"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    Get("/todos", "TodosController@show").name("todos"),
    Get("/todos/@id:int", "TodosController@single").name("single.todo"),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
