#!/usr/bin/env python
# coding: utf-8

# ## Automatizando processo de Gravação

# In[ ]:


fileName = input('Digite o nome do aquivo ')


# In[ ]:


fileName = fileName + ".txt"


# In[ ]:


arql3 = open(fileName, "w")


# In[ ]:


arql3.write("Aquivo criado com sucesso")


# In[ ]:


arql3.close()


# In[ ]:


arql3 = open(fileName, 'r')


# In[ ]:


print(arql3.read())


# In[ ]:


arql3.close()


# # Abrindo DataSet
# ### link de dados:  https://data.cityofchicago.org/

# In[30]:


f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")


# In[31]:


data = f.read()


# In[32]:


rows = data.split('\n')


# In[33]:


print(rows)


# ### DataSet em Colunas

# In[35]:


f = open('tratamentos-de-arquivos/arquivos/salarios.csv', "r")


# In[36]:


data = f.read()


# In[37]:


rows = data.split('\n')


# In[38]:


full_data = []


# In[40]:


for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)


# In[41]:


print(full_data)


# In[ ]:




