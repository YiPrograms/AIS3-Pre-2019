import pickle

with open("user.pickle", "rb") as f:
    a = pickle.load(f)

print(a)