from multiprocessing import sharedctypes, Process
from numpy import ctypeslib


def fill_arr(arr_view, i):
    arr_view.fill(i)


def main():
    ra = sharedctypes.RawArray('i', 4)
    arr = ctypeslib.as_array(ra)
    arr.shape = (2, 2)
    p1 = Process(target=fill_arr, args=(arr[:1, :], 1))
    p2 = Process(target=fill_arr, args=(arr[1:, :], 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print (arr)


if __name__ == '__main__':
    main()
