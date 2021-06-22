#!/usr/bin/env python
# coding: utf-8

# ##
# inuron---> MatPlotLib ---> Python
# 
# #In this assignment students have to transform iris data into 3 dimensions
# #and plot a 3d chart with transformed dimensions and colour each data
#  point with specific class.##

# In[3]:




import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets


# In[4]:


iris = sns.load_dataset("iris")
iris


# In[5]:


ax = plt.axes(projection ='3d')
x = list(iris['sepal_length'])
y = list(iris['sepal_width'])
z = list(iris['petal_width'])

ax.plot3D(x,y,z,'green')
plt.show()

