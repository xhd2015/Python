from mocker import Mocker

mocker = Mocker()

def setup():
    fake_time = mocker.replace('time.time')

    fake_time()
    mocker.result(1.0)
    fake_time()
    mocker.result(1.1)
    fake_time()
    mocker.result(1.2)

    mocker.replay()

def teardown():
    mocker.restore()
    mocker.verify()
