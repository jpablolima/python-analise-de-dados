#!/usr/bin/env python
# coding: utf-8

# # Method and Functions

# In[4]:


lst = [10,100,500]
#dir(lst)


# # variáveis locais e global

# In[5]:


# Functions - variáveis locais e global

var_global = 10 # Global


def sum(number1, number2):
    var_local = number1 + number2 # local
    print(var_local)
sum(5,25)


# In[6]:


print(var_global)


# In[8]:


# Functions Buil-in
abs(-56)


# In[11]:


# Converter a função int para converter o valor digitado
age = int(input("Enter your age: "))
if(age > 15):
    print('Age')


# In[34]:


# Verificando se um número é primo - Math
import math
def numPrimo(num):
    ''' verificando se um número é primo'''
    if(num  % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"
numPrimo(541)


# # Expressões Lambda
# 

# In[37]:


potencia = lambda num: num**2
potencia(5)


# In[39]:


temp = 40
while temp > 35:
    print(temp)
    temp = temp -1


# In[40]:


listB = [32,53,85,10,15,17,19]
soma = 0
for i in listB:
    double_i = i * 2
    soma += double_i
    print(soma)

