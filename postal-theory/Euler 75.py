#!/usr/bin/env python
# coding: utf-8

# ## PROJECT 75

# In[1]:


from math import gcd, sqrt
L = 1500001
maybe = set()
nope = set()
for m in range(2, int(sqrt(L/2))):
    for n in range(m-1, 0, -2):
        if gcd(m, n) == 1:
            s = 2*(m*m + m*n)
            for k in range(1, int(L/s+1)):
                nope.add(k*s) if k*s in maybe else maybe.add(k*s)
print (len(maybe-nope))


# In[ ]:




