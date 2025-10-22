li = [7,6,78,3,5,12,67,45,23]
tu = (5,7,6,23,12,78,4,45,45)

common = list(set(li) & set(tu))

all_elements = list(set(li) | set(tu))


print("Common elements: ", common)
print("All elements: ", all_elements)