from orator.seeds import Seeder
from app.Todo import Todo
from config.factories import factory 


class TodoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        factory(Todo, 50).create()

