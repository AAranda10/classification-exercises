#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import env
import os


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.DataFrame(pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db')))

get_titanic_data().head()


# In[2]:


def get_iris_data():
    return pd.DataFrame(pd.read_sql('SELECT * FROM measurements JOIN species on measurements.species_id = species.species_id', get_connection('iris_db')))
get_iris_data().head()


# In[3]:


def my_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.DataFrame(pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db')))
        df.to_csv(filename, index = False)
        return df
my_titanic_data().head()


# In[4]:


def my_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.DataFrame(pd.read_sql('SELECT * FROM species', get_connection('iris_db')))
        df.to_csv(filename, index = False)
        return df
my_iris_data().head()


# In[ ]:





# In[ ]:




