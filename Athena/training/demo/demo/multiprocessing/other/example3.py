
from multiprocessing import Process, Pipe

def func(conn):
    conn.send(dict(value=100, name='foo'))
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    proc = Process(target=func, args=(child_conn,))
    proc.start()
    print parent_conn.recv()
    proc.join()
