"""Exercise the Point class."""


import point

origin = point.Point()
p1 = point.Point(2, 3)
p2 = point.Point(-2, -3)

print(origin)
print(p1)
print(p2)
print()
print(origin.__repr__())
print(p1.__repr__())
print(p2.__repr__())
print()
print(origin.euclidian_distance(p1))
print(origin.manhattan_distance(p1))
print()
print(origin.add(p1))
print(p1.add(p2))
print()
print(origin + p1)
print(p1 + p2)
print(origin + p1 + p2)
