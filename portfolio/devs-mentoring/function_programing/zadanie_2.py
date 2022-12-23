to_sort = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
to_sort_2 = to_sort.copy()
to_sort.sort(key=lambda x: x[1])
print(to_sort)
print(to_sort_2)
print(sorted(to_sort_2, key=lambda x: x[1]))
print(to_sort_2)

# pure function- dlatego chyba sorted lepszy?
