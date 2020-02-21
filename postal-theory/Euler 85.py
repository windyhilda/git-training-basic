#https://blog.dreamshire.com/project-euler-85-solution/
#!/usr/bin/env python
# coding: utf-8

# ## PROJECT 85

# In[1]:


L = min_diff = 2000000;

for x in range(2, 101):
  for y in range(x, 101):
    diff = abs(x*(x + 1) * y*(y + 1) / 4 - L)
    if diff < min_diff:
      area, min_diff = x * y, diff

print ("Project Euler 85 Solution =", area)


# In[ ]:




