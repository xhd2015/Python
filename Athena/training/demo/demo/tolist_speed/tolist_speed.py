import timeit

t_tolist = timeit.Timer("b=a.tolist()", "import numpy;a=numpy.arange(1e6)")
print t_tolist.repeat(repeat=3, number=10)


t_list = timeit.Timer("b=list(a)", "import numpy;a=numpy.arange(1e6)")
print t_list.repeat(repeat=3, number=10)
