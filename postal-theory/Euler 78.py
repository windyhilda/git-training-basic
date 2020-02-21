#Author Zach Denton
#https://zach.se/project-euler-solutions/78/

#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 78

# In[1]:


from itertools import *

def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, list(range(-250, 250))))[1:]
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) for sign, p in zip(signs, pentagonals))

    return partitions[n]

def main():
    print(next((n for n in count(0) if partition(n) % 1000000 == 0)))
    
print(main())


# In[ ]:




