def combs(a):
    print('a', a)
    
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[:-1]):
        cs += [c, c+[a[-1]]]
    return cs
    
cs = combs([1,2,3,4,5])
print(cs)
