class Foo(object):
    def __init__(self, first=True):
        self.first = first

    def __bool__(self):
        if self.first:
            self.first = False
            return True
        return False
    
    def __len__(self):
        return 0