from mocker import Mocker
from datetime import datetime

mocker = Mocker()

def setup():
    fake_datetime = mocker.replace(datetime)

    fake_datetime.now()
    mocker.result(datetime(year = 2009, month = 6, day = 12,
                           hour = 10, minute = 15, second = 5))
    mocker.count(1, None)

    mocker.replay()

def teardown():
    mocker.restore()
    mocker.verify()
