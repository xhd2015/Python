import multiprocessing as mp

a = 10.0
b = 'this is a string!!!'

def worker():
    global a
    global b
    print a
    print b
    a = 12.0
    print a

if __name__ == '__main__':
    p1 = mp.Process(target=worker)
    p2 = mp.Process(target=worker)

    p1.start()
    p1.join()

    p2.start()
    p2.join()
