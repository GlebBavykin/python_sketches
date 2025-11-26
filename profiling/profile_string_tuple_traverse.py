from time import time

ts = time()
for i in range(1, 1000000):
    a = "!@#$%^&*()_+".find("+")
te = time()
print("Find Sting Took: %0.9f sec" % (te - ts))

ts = time()
for i in range(1, 1000000):
    a = b"!@#$%^&*()_+".find(b"+")
te = time()
print("Find Byte Sting Took: %0.9f sec" % (te - ts))

ts = time()
for i in range(1, 1000000):
    a = "+" in "!@#$%^&*()_+"
te = time()
print("Sting Took: %0.9f sec" % (te - ts))

tst = time()
for i in range(1, 1000000):
    b = "+" in ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+")
tet = time()
print("Tuple Took: %0.9f sec" % (tet - tst))

tsl = time()
for i in range(1, 1000000):
    c = "+" in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
tel = time()
print("List Took: %0.9f sec" % (tel - tsl))

tsts = time()
for i in range(1, 1000000):
    d = "+" in {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"}
tets = time()
print("Set Took: %0.9f sec" % (tets - tsts))

ts = time()
for i in range(1, 1000000):
    a = b"+" in b"!@#$%^&*()_+"
te = time()
print("Byte Sting Took: %0.9f sec" % (te - ts))

ts = time()
for i in range(1, 1000000):
    a = "+" in "!@#$%^&*()_+"
te = time()
print("Just Sting Took: %0.9f sec" % (te - ts))
