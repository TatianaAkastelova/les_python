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


list1 = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3, 9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
list_ = []
for elem in list1:
     types = [(type(sym)).__name__ for sym in elem if (type(sym)).__name__]
     single_types = []
     single_types = [i_types for i_types in types if i_types not in single_types]
     types_count = [types.count(element_type) for element_type in single_types]
     max_types_count = max(types_count)
     index_max = types_count.index(max(types_count))
     main_type = single_types[index_max]
     separated_list = [element for element in elem if type(element).__name__ == main_type]
     list_.extend(separated_list)
res_int_lst = [k for k in list_ if type(k) == int]
res_float_lst = [k for k in list_ if type(k) == float]
res_str_lst = [k for k in list_ if type(k) == str]
print("clean list", list_)
print("int", res_int_lst)
print("float", res_float_lst)
print("string", res_str_lst)