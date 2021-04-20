list1 = [
        [1, None, 2, 3, 4+5j, 6],
        [1.0, 2.5, None, 3, 9, 4.0+5.2j, 6.1],
        ['1', '2', '3.6', None, '4+5.7j', '6']
        ]

list1 = [list1[j] for j in range(0, len(list1)) if type (list1[j]). __name__ == "int"]
print(list1)
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
