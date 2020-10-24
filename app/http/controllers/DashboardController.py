""" A DashboardController Module """

from masonite.controllers import Controller


class DashboardController(Controller):
    """Class Docstring Description
    """

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", DashboardController)
        """

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", DashboardController)
        """

        pass

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", DashboardController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", DashboardController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", DashboardController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", DashboardController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", DashboardController)
        """

        pass