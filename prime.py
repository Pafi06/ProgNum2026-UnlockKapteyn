#!/usr/bin/env python
# coding: utf-8

# In[20]:


def getprimes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
            else:
                primes.append(num)
        num += 1
    return primes

plist = getprimes(60)
t = [15, 37, 60]

for p in t:
    print({plist[p-1]})


# In[ ]:





# In[ ]:




