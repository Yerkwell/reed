from itertools import product
import re

def get_vars_list(varias):
    v = []
    for i in range(varias):
        v.append(['x' + str(i), '1'])

    vs = list(product(*v))

    vvs = list(map(lambda x: [x, '0'], vs))

    pr = list(map(lambda x: list(x),list(product(*vvs))))

    s = ""

    for n,i in enumerate(pr):
        for m,j in enumerate(pr[n]):
            if isinstance(j, tuple):
                pr[n][m] = '*'.join(j)
        pr[n] = '+'.join(i)

def print_vars(varias):
    pr = get_vars_list(varias)
    pr = list(map(lambda x: re.sub(r'\+0','',x) ,pr))
    pr = list(map(lambda x: re.sub(r'^0\+','',x), pr))
    pr = list(map(lambda x: re.sub(r'\*1','',x), pr))
    pr = list(map(lambda x: re.sub(r'^1\*','',x), pr))
    pr = list(map(lambda x: re.sub(r'\+1\*','+',x),pr))

    s = '\n'.join(pr)

    with open("bools.txt", "w") as file:
        file.write(s)
    print('Done')

def sum(l1,l2):
    l3 = []
    for i in range(len(l1)):
        l3.append((l1[i] + l2[i]) % 2)
    return l3

def reed(l):
    ll = len(l)
    if ll == 1:
        return l
    l1 = l[:int(ll/2)]
    l2 = l[int(ll/2):]
    l2 = sum(l1,l2)
    return rid(l1) + rid(l2)
    
print(reed([1,0,1,1,0,0,0,1]))
