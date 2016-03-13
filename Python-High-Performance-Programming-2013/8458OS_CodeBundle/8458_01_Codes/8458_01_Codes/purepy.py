import random
from collections import Counter

# Comparing a Counter with a standard loop
def counter_1(): 
    items = [random.randint(0, 10) for i in range(10000)] 
    return Counter(items) 

def counter_2(): 
    items = [random.randint(0, 10) for i in range(10000)] 
    counter = {} 
    for item in items: 
        if item not in counter: 
            counter[item] = 0 
        else: 
            counter[item] += 1 

def loop(): 
    res = [] 
    for i in range(100000): 
        res.append(i * i) 
    return sum(res) 

def comprehension(): 
    return sum([i * i for i in range(100000)]) 

def generator(): 
    return sum(i * i for i in range(100000))

