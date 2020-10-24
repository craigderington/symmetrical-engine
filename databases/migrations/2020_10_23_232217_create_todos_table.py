from orator.migrations import Migration


class CreateTodosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('todos') as table:
            table.increments('id')
            table.string('name')
            table.text("description")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.timestamp('verified_at').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
