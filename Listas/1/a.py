a = [1, 2, 3]
a is a
a + [] is a
a + [] == a
[10, 20, 3] > [1, 2, 3]
[10, 2, 3] > [1, 2, 3]­
[1, 20, 30] > [1, 2, 3]­
[0, 2, 3] <= [1, 2, 3]­
[1] < [2, 3]­
[1] < [1, 2]­
[1, 2] < [0]
a = list(range(1, 4))
print(a)
[1, 2] == [1, 2]
[1, 2] is [1, 2]
a = [1, 2, 3]
b = [a[0], a[1], a[2]]
a == b
a is b
a[0] == b[1]
b is [b[0], b[1], b[2]]