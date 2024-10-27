
man = ("sayan", "abishek", "vivek", "sumit")

print("Length of tuple:", len(man))
print("Type of tuple:", type(man))

add = ("Sneha",)
man = man + add
print("Updated tuple:", man)

def remove_from_tuple(tpl, value):
    return tuple(item for item in tpl if item != value)

man = remove_from_tuple(man, "abishek")
print("Tuple after removal:", man)
