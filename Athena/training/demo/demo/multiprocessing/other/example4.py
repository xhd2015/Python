
from multiprocessing import Process, Value, Array

def func(num, arr):
    num.value = 355/113.
    for i in range(len(arr)):
        arr[i] = arr[i]**2

if __name__ == "__main__":
    n = Value('d', 0.0)
    a = Array('i', range(10))
    proc = Process(target=func, args=(n, a))
    proc.start()
    proc.join()
    print n.value
    print a[:]
