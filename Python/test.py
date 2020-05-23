# import itertools
# s = "cbaebabacd"
# print(s)
# print(type(s))
# p = "abc"
# p_list = list(p)
# p_ang = itertools.permutations(p_list)
# ang_list = []
# for k in p_ang:
#     ang_list.append(''.join(k))

# for ang in ang_list:
#     print(ang)
#     print(type(ang))
#     print(s.find(ang))
# for i in range(7):
#     print(i, (i+2)%7)
from bisect import bisect_left
l = list(range(5))
for i in range(7):
    print(i, bisect_left(l,i))