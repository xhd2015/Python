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

    def __eq__(self, other):
        return self.name == other.name and self.begins == other.begins and self.ends == other.ends

    def __ne__(self, other):
        return not self.__eq__(other)

class activities(_tasks):
    def excludes(self, other):
        return isinstance(other, activities)


class statuses(_tasks):
    def excludes(self, other):
        return False

class schedules:
    def __init__(self, name = 'schedule'):
        self.tasks = []
        self.name = name

    def add(self, task):
        for contained in self.tasks:
            if task.overlaps(contained):
                if task.excludes(contained) or contained.excludes(task):
                    raise schedule_error('"%s" overlaps with "%s"' %
                                         (task.name, contained.name))

        self.tasks.append(task)

    def remove(self, task):
        try:
            self.tasks.remove(task)
        except ValueError:
            pass

    def __contains__(self, task):
        return task in self.tasks

    def store(self, storage):
        for task in self.tasks:
            storage.store_object(self.name, task)

    @staticmethod
    def load(storage, name = 'schedule'):
        value = schedules(name)

        for task in storage.load_objects(name):
            value.add(task)

        return value
