from mocker import Mocker, MockerTestCase, ANY
from planner.data import schedules
from planner.persistence import file
from os import unlink

def unpickle_mocked_task(begins):
    mocker = Mocker()
    ret = mocker.mock()
    ret.overlaps(ANY)
    mocker.result(False)
    mocker.count(0, None)
    ret.begins
    mocker.result(begins)
    mocker.count(0, None)
    mocker.replay()
    return ret
unpickle_mocked_task.__safe_for_unpickling__ = True

class test_schedules_and_file(MockerTestCase):
    def setUp(self):
        mocker = self.mocker

        A = mocker.mock()
        A.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        A.begins
        mocker.result(5)
        mocker.count(0, None)
        A.__reduce_ex__(ANY)
        mocker.result((unpickle_mocked_task, (5,)))
        mocker.count(0, None)

        B = mocker.mock()
        B.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        B.begins
        mocker.result(3)
        mocker.count(0, None)
        B.__reduce_ex__(ANY)
        mocker.result((unpickle_mocked_task, (3,)))
        mocker.count(0, None)

        C = mocker.mock()
        C.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        C.begins
        mocker.result(7)
        mocker.count(0, None)
        C.__reduce_ex__(ANY)
        mocker.result((unpickle_mocked_task, (7,)))
        mocker.count(0, None)

        self.A = A
        self.B = B
        self.C = C

        mocker.replay()

    def tearDown(self):
        try:
            unlink('test_schedules_and_file.sqlite')
        except OSError:
            pass

    def test_save_and_restore(self):
        sched1 = schedules()

        sched1.add(self.A)
        sched1.add(self.B)
        sched1.add(self.C)

        store1 = file('test_schedules_and_file.sqlite')
        sched1.store(store1)

        del sched1
        del store1

        store2 = file('test_schedules_and_file.sqlite')
        sched2 = schedules.load(store2)

        self.assertEqual(set([x.begins for x in sched2.tasks]),
                         set([3, 5, 7]))
