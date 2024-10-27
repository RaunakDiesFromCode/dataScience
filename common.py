s1 = [1, 2, 3, 4, 5, 6, 7]
s2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

set1 = set(s1)
set2 = set(s2)

intersection = list(set1 & set2)

print("Common elements are: ", intersection)