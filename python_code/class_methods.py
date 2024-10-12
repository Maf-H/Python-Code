#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from random import randint

name = ["አድዋ", "ምኒልክ", "ተዋነይ"]
etta = []
for i in range(64):
    etta.append(name[randint(0, 2)])
print("አድዋ: ", etta.count("አድዋ"))
print("ምኒልክ: ", etta.count("ምኒልክ"))
print("ተዋነይ: ", etta.count("ተዋነይ"))


class Sample:
    def __init__(self):
        self.name = Sample.__name__

    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()


class A:
    def __init__(self, v=1):
        self.v = v

    def set(self, v):
        self.v = v
        return v


a = A()
print(a.set(a.v + 1))


class A:
    A = 1


print(hasattr(A, 'A'))


class A:
    def __str__(self):
        return 'a'


class B(A):
    def __str__(self):
        return 'b'


class C(B):
    pass


o = C()
print(o)


class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


try:
    for x in I():
        print(x, end='')
except StopIteration as err:
    print(err)
print()



