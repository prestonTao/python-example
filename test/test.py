


def p(p,day=1):
    print(day)


params = {"day":21}

p(params)



u = '1'


print(cmp(u,'1'))
print(cmp(u,'2'))
print(cmp(u,'7'))


params = {'name':'tao','age':18}

print('name' in params)

print '1  ###############################################################'

class Base():
    name = "tao"
    def __init__(self,value=None):
        self.age = 18
        self.name = value
    def foo(self):
        print self.name,self.age

b = Base()
b.foo()
b.age = 19
b.name = "taopopoo"
b.foo()


class Base_b():
    name = "tao"
    def __init__(self, *args):
        self.age = 18
    def foo(self):
        print self.name,self.age

bb = Base_b(age = 19)
bb.foo()

print '###############################################################'

def excption(method):
    try:
        result = method()
        if result :
            return result
    except Exception,e:
        print e
        return e

@excption
def exportE():
    print 'tao'

# exportE()