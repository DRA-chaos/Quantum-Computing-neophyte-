#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qiskit


# In[1]:


from qiskit import * 


# In[3]:


from qiskit.visualization import plot_bloch_vector


# In[4]:


import matplotlib as plt


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


#“Spin-Up” state on the Bloch Sphere


# In[7]:


plot_bloch_vector([0,0,1], title="Spin-Up")


# In[8]:


#“Spin-Down” state on the Bloch Sphere


# In[11]:


plot_bloch_vector([0,0,-1], title="Spin-Down")


# In[14]:


plot_bloch_vector([0,1,0], title="Spin-Right")


# In[15]:


#createing  a quantum circuit in QISKit 


# In[17]:


circuit.barrier()
circuit.draw(output='mpl')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:




