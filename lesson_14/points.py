class Point:
    s = 'Attribute of class'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt1 = Point()
print(pt1.x, pt1.y)
pt2 = Point(3, 6)
print(pt2.x, pt2.y)
pt3 = Point(5)
print(pt3.x, pt3.y)

pt1.x = 9
print(pt1.x)
print(pt2.x, pt2.y)
print(pt3.x, pt3.y)

print(pt1.s)
print(pt2.s)
print(pt3.s)

pt1.s = 'New string'

print(pt1.s)
print(pt2.s)
print(pt3.s)

Point.s = 'New attribute of class'

print(pt1.s)
print(pt2.s)
print(pt3.s)


