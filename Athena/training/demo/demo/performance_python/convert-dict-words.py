import time
words = open('/usr/share/dict/words').read().split()

def basic_loop(words):
    uwords = []
    for word in words:
        uwords.append(word.upper())
    return uwords

def eliminate_dots(words):
    upper = str.upper
    uwords = []
    append = uwords.append
    for word in words:
        append(upper(word))
    return uwords

def use_map(words):
    return map(str.upper, words)

def list_comp(words):
    return [w.upper() for w in words]

def timing(f, n, a):
    print f.__name__,
    r = range(n)
    t1 = time.clock()
    for i in r:
        f(a); f(a);
    t2 = time.clock()
    print round(t2-t1, 2)

testfuncs = basic_loop, eliminate_dots, use_map, list_comp
for f in testfuncs: timing(f, 5, words)
