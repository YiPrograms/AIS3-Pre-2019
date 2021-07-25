

class Foo():
    def hi(self):
        global Moo
        class Moo():
            x = 1

a = Foo()

a.hi()

b = Moo()
print(b.x)