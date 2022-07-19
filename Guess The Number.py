#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random


# In[12]:


num = random.randint(0,20)
print(num)


# In[13]:


guess_str = input("Guess the number: ")
guess_num = int(guess_str)
if guess_num < num:
    print("Oh no! Your guess is too low.")
elif guess_num > num:
    print("Welp! Your guess is too high.")
else:
    print("Correct! Nice guessing skills.")


# In[ ]:





# In[ ]:




