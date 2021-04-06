school = {'5a':10, '5b':12, '6a':9, '6b':10, '6c':12, '7a':12, '8a':7, '8b':9, '9a':5, '9b':6, '9c':5}
school ['5a'] = 11
print(school)
school ['5c'] = 15
del school ['6b']
print(sum(school.values()))


dct = {1: 'a', 2: 'c', 3: 'b'}
def rev_key(dct):
    dct_new = dict()
    for i, v in dct.items():
        for w in v:
            dct_new[w] = dct_new.get(w, []) + [i]
    return dct_new
print(rev_key(dct))


