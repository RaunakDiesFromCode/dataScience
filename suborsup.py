s1 = [1, 2, 3, 4, 5, 6, 7]
s2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 1, 2, 3, 4, 5, 6, 7]

set1 = set(s1)
set2 = set(s2)

if (set2 > set1):
    print("set 2 is superset")
else:
    print("set 1 is superset")