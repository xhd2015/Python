def setup():
    import time
    time.connection = 5

def teardown():
    import time
    del time.connection

