set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
print(set1 & set2 & set3)
print(set1 - set2 - set3)
print(set1 | set2 | set3)


sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet |= set(sampleList)
print(sampleSet)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 & set2)
print(set1 | set2)
print(set1.difference(set2))


set1 = {10, 20, 30, 40, 50}
set1.remove(10)
set1.remove(20)
set1.remove(30)
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1 & set2)
result = set1.update(set2)
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.symmetric_difference_update(set2)
print(set2)


list1 = [
        [1, None, 2, 3, 4+5j, 6],
        [1.0, 2.5, None, 3, 9, 4.0+5.2j, 6.1],
        ['1', '2', '3.6', None, '4+5.7j', '6']
        ]

list1_int = []
list1_float = []
list1_str = []
for item in list1:
    types = []
    for elem in item:
        elem_type = type(elem)
        types.append(elem_type.__name__)
    single_types = []
    for i_type in types:
        if i_type not in single_types:
            single_types.append(i_type)
    types_count = []
    for element_type in single_types:
        type_count = types.count(element_type)
        types_count.append(type_count)

        max_type_count = max(types_count)
        index_max = types_count.index(max(types_count))
        main_type = single_types[index_max]

    separated_list1 = []
    for element in item:
        if type(element).__name__ == main_type:
            separated_list1.append(element)
    list1_int.extend(separated_list1)
    list1_float.extend(separated_list1)
    list1_str.extend(separated_list1)
print("list1_int:", list1_int)
print("list1_float:", list1_float)
print("list1_str:", list1_str)

in_list1_int = []
for i in list1_int:
    if type(i) == int:
        in_list1_int.append(i)
print("in_list1_int:",  in_list1_int)
in_list1_float = []
for i in list1_float:
    if type(i) == float:
        in_list1_float.append(i)
print("in_list1_float:", in_list1_float)
in_list1_str = []
for i in list1_str:
    if type(i) == str:
        in_list1_str.append(i)
print("in_list1_str:", in_list1_str)
