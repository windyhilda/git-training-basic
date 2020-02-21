#!/usr/bin/env python
# coding: utf-8

# ## PROBLEM 80

# In[4]:


#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #80


from math import sqrt
from decimal import *

#the easy code
getcontext().prec = 105
s = 0
for i in range(1, 101):
    if sqrt(i) != int(sqrt(i)):
        st = str(Decimal(i).sqrt())
        s += sum(int(c) for c in st.replace('.', '')[:100])
print (s)


# In[ ]:




