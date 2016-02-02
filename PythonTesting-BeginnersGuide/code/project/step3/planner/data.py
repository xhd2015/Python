from datetime import timedelta

class task_error(Exception):
    pass

class schedule_error(Exception):
    pass

class _tasks:
    def __init__(self, name, begins, ends):
        if ends < begins:
            raise task_error('The begin time must precede the end time')
        if ends - begins < timedelta(minutes = 5):
            raise task_error('The minimum duration is 5 minutes')

        self.name = name
        self.begins = begins
        self.ends = ends

    def excludes(self, other):
        raise NotImplemented('Abstract method. Use a child class.')

    def overlaps(self, other):
        if other.begins < self.begins:
            return other.ends > self.begins
        elif other.ends > self.ends:
            return other.begins < self.ends
        else:
            return True

    def __repr__(self):
        return ''.join(['<', self.name,
                        ' ', self.begins.isoformat(),
                        ' ', self.ends.isoformat(),
                        '>'])

class activities(_tasks):
    def excludes(self, other):
        return isinstance(other, activities)


class statuses(_tasks):
    def excludes(self, other):
        return False

class schedules:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        for contained in self.tasks:
            if task.overlaps(contained):
                if task.exclude(contained) or contained.exclude(task):
                    raise schedule_error(task, containeed)

        self.tasks.append(task)

    def remove(self, task):
        try:
            self.tasks.remove(task)
        except ValueError:
            pass

    def __contains__(self, task):
        return task in self.tasks

