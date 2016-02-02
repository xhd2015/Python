class FootballRushIterator(object):
    def __init__(self, count=5):
        self.count = count

    def __iter__(self):
        self._counter = 1
        return self
        
    def next(self):
        if self._counter <= self.count:
            result = "%d %s" % (self._counter, "mississippi")
            self._counter += 1
            return result
        else:    
            raise StopIteration

# Just to show that Iterators are easier with generator syntax
def get_rusher(count=5):
    for i in range(1,count+1):
        yield "%d mississippi" % i

if __name__ == "__main__":
    rush_iterator = FootballRushIterator()
    
    for value in rush_iterator:
        print value            
