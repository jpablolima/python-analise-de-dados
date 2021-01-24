#!/usr/bin/env python
# coding: utf-8

# # Explotrando DataSet Boston housing dataset

# In[11]:


# importação dos módulos necessários
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


# carregar Boston housing
from sklearn.datasets import load_boston
boston = load_boston()


# In[13]:


type(boston)


# In[14]:


# Visualizando o shape do dataSet
boston.data.shape


# In[15]:


# Descrição do DataSet
print(boston.DESCR)


# In[16]:


print(boston.feature_names)


# In[17]:


# convertendo o dataSet em um DataFrame pandas
df = pd.DataFrame(boston.data)
df.head()


# In[18]:


# convertendo  o título das colunas
df.columns = boston.feature_names
df.head()


# In[19]:


df.describe()


# In[20]:


# Dados em um array com preços das  casas
boston.target


# In[21]:


# Adicionando o preço da casa ao DataFrame
df['PRICE'] = boston.target
df.head()


# # Prevendo Preços das Casas em Boston

# In[22]:


# importando o módulo de regressão linear
from sklearn.linear_model import LinearRegression


# In[23]:


# removendo preço da casa como variável depedente
x = df.drop('PRICE', axis = 1)


# In[24]:


# Definindo y
y = df.PRICE


# In[25]:


plt.scatter(df.RM, y)
plt.xlabel('Média do Número de Quartos por Casa')
plt.ylabel('Preço da Casa')
plt.title('Relaçãoe em Números de Quartos e Preço')
plt.show()


# In[26]:


# Criando objeto de regressãp Linear
regr = LinearRegression()


# In[27]:


type(regr)


# In[28]:


# Treinando o modelo
regr.fit(x,y)


# In[29]:


# Coeficientes
print('Coeficiente: ',regr.intercept_)
print('Número de Coeficientes: ', len(regr.coef_))


# In[30]:


# Prevendo o preço das casas
regr.predict(x)


# In[31]:


# Coparando preços originais x preços previstos
plt.scatter(df.PRICE, regr.predict(x))
plt.xlabel('Preço Orginal')
plt.ylabel('Preço Previsto')
plt.title('Preço original x Preço Previsto')
plt.show()


# In[32]:


# Verificar possíveis erros na prsdição dos preços das casas
msel = np.mean((df.PRICE - regr.predict(x)) ** 2)
print(msel)


# In[33]:


# Aplicando regressão linear para uma variavel  e calculando MSE
regr = LinearRegression()
regr.fit(x[['PTRATIO']], df.PRICE)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




