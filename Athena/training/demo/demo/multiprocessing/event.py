import multiprocessing as mp


def wait_on_event(e):
    name = mp.current_process().name
    e.wait()
    print name, "finished waiting"


if __name__ == '__main__':
    e = mp.Event()
    ps = [mp.Process(target=wait_on_event,
                     args=(e,))
          for i in range(10)]
    [p.start() for p in ps]
    print "e.is_set()", e.is_set()
    raw_input("press any key to set event")
    e.set()
    [p.join() for p in ps]
