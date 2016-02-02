
from datetime import date, timedelta
from traits.api import HasTraits, Str, Date


class Task(HasTraits):
    """A task to be performed."""

    # Description of the task.
    description = Str

    # Due date of the task.
    due_date = Date

    def _due_date_default(self):
        """Default due date is one week from today."""
        return date.today() + timedelta(days=7)


if __name__ == "__main__":
    task = Task(description="File taxes")
    print "Due date (default) is", task.due_date
    task.due_date = date(2012, 4, 15)
    print "Due date is now", task.due_date
