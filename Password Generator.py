#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the required libraries.
import random
import string


# In[2]:


#generating the length of the password whilst making sure it is of type int.
length = input("Hello! Welcome to Finesse Online Password Generator.\nKindly type in the desired length of your password: ")
def check_user_input(length):
    try:
        length = int(length)
    except ValueError:
        try:
            length = float(length)
            print("Error! Decimal detected. Input must be an integer.")
        except ValueError:
            print("Error! Invalid input. Input must be an integer.")
check_user_input(length)
length = int(length)


# In[3]:


#generating the number of letters in the password whilst making sure it is of type int.
letter_num = input("How many letters do you want in your password? ")
check_user_input(letter_num)
letter_num = int(letter_num)


# In[4]:


#generating the number of digits in the password whilst making sure it is of type int.
num = input("How many numbers do you want in your password? ")
check_user_input(num)
num = int(num)


# In[5]:


#making sure the length of password is a minimum of 6 characters long.
if length < 6:
    print("Error! Password should contain at least 6 characters.")
else: #making sure the sum of desired letters and numbers do not exceed nor is equal to the length of password.
    if letter_num + num > length:
        print("Error! Sum of letter and number is more than length of password.")
    elif letter_num + num == length:
        print("Error! Sum of letter and number is equal to length of password. Password must contain symbol.")
    else: #generating the number of symbols in the password.
        symbol_num = length - (letter_num + num)


# In[6]:


#generating a list of randomly selected letters of length previously specified.
letters = string.ascii_letters #builds a list of all possible letters.
gen_letters = random.choices(letters, k=letter_num)
gen_letters


# In[7]:


#generating a list of randomly selected numbers of length previously specified.
num_list = string.digits #builds a list of all possible digits.
gen_num = random.choices(num_list, k=num)
gen_num


# In[8]:


#generating a list of randomly selected symbols of length previously calculated.
symbols = string.punctuation #bulds a list of all possible symbols.
gen_symbols = random.choices(symbols, k=symbol_num)
gen_symbols


# In[9]:


#generates the password.
final_list = gen_letters + gen_num + gen_symbols #combines the three lists created in the above cells.
random.shuffle(final_list) #shuffles the elements in the final list.
password = ''.join(final_list) #joins the elements in the shuffled list to form a single string which is the password.
password

