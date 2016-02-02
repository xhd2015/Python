# global variable
var = 0


class MyClass(object):
    # class variable
    var = 1

    def access_class_c(self):
        print 'class var:', self.var

    def access_global_c(self):
        global var
        print 'global var:', var

    def write_class_c(self):
        MyClass.var = 2
        print 'class var:', self.var

    def write_instance_c(self):
        self.var = 3
        print 'instance var:', self.var


obj = MyClass()
obj.access_class_c()
obj.access_global_c()
obj.write_class_c()
obj.write_instance_c()
