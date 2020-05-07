#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
cust_df=pd.read_csv("Cust_Segmentation.csv")
cust_df.head()


# In[2]:


df=cust_df.drop('Address', axis=1)
df.head()


# In[3]:


from sklearn.preprocessing import StandardScaler
import numpy as np
x=df.values[:,1:]
x=np.nan_to_num(x)
Clus_dataSet=StandardScaler().fit_transform(x)
Clus_dataSet


# In[12]:


from sklearn.cluster import KMeans
clusterNum=3
k_means=KMeans(init="k-means++", n_clusters=clusterNum, n_init=12)
k_means.fit(x)
labels=k_means.labels_
print(labels)


# In[13]:


df["Clus_km"]=labels
df.head(5)


# In[14]:


df.groupby('Clus_km').mean()


# In[28]:


import matplotlib.pyplot as plt
area=np.pi*(x[:, 1])**2
plt.scatter(x[:, 0], x[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Inccome', fontsize=16)

plt.show()


# In[30]:


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')

ax.scatter(x[:, 1], x[:, 0], x[:, 3], c=labels.astype(np.float))

