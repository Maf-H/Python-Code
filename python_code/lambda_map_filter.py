#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from random import seed, randint


list_1 = [x for x in range(5)]
list_2 = list(map(lambda z: 2**z, list_1))
print(list_1)
print(list_2)

for rrr in map(lambda y: y*y, list_2):
    print(rrr, end=' ')
print("\n")

for x in map(lambda x: x % 2 != 0, list_1):
    print(x, end=', ')
print()

seed()
data = [randint(-10, 10) for x in range(5)]  # generates random numbers from [-10, 10]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))  # we change to list because map function returns
                                                               # non iterable generator

print(data)
print(filtered)


students = [("Gizachew", 'D', 26),
            ("Marta", 'B', 33),
            ("Mesfin", 'A', 31),
            ("Fitih", 'C', 7),
            ("Menilik", 'F', 1)]

# students.sort()   # sorts the list in alphabetical order
# students.sort(reverse=True)  # sorts the list in reverse alphabetical order
old_students = list(map(lambda grade: (grade[0], grade[1], grade[2]*2), students))  # used to sort with columns value
print('==========================')
for i in old_students:
    print(i)
