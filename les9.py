l = {1, 3, 4, 5}
print(all(l))
l = {0, False}
print(all(l))
l_0 = {1, 3, 4, 0}
print('l_0: ', all(l_0))
l = {1, False, 5}
print(all(l))
l = set()
print('type(l): ', type(l))
print(all(l))


l = {1, 3, 4, 0}
print(any(l))
l = {0, False}
print(any(l))
l = {0, False, 5}
print(any(l))
l = set()
print(any(l))


grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))


testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))
testSet = set()
print(testSet, 'length is', len(testSet))


languages = {"Python", "C Programming", "Java", "JavaScript"}
largest_string = max(languages)
smallest_string = min(languages)
print("The largest string is:", largest_string)
print("The smallest string is:", smallest_string)


py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))


numbers = {2.5, 3, 4, -5}
numbers_sum = sum(numbers)
print(numbers_sum)
numbers_sum = sum(numbers, 10)
print(numbers_sum)
