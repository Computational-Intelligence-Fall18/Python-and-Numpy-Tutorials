
# coding: utf-8

# # 0. Import Numpy

# In[1]:


import numpy as np


# In[3]:


np.__version__


# **Initialize using python list:**

# In[4]:


a = np.array([1,2,3]) 


# In[5]:


print(a)


# In[6]:


b = np.array([[1,2],[3,4]])
print(b)


# **Initialize using some NumPy functions:    **

# In[7]:


c = np.zeros((2,3))
print(c)


# In[8]:


d = np.ones((3,4))
print(d)


# In[9]:


e = np.arange(2,10,2)
print(e)


# In[10]:


f = np.linspace(0,100,6)
print(f)


# In[11]:


g = np.full((2,3), 6)
print(g)


# In[12]:


h = np.eye(3)
print(h)


# In[13]:


i = np.eye(3,4)
print(i)


# **Random Initialization:**

# In[14]:


j = np.random.rand(4,5) # samples from a uniform distribution over [0, 1)
print(j)


# In[15]:


k = np.random.randint(2,5,size = (2,3))#samples from discrete uniform distribution in the specified half-open interval
print(k)


# In[16]:


mu, sigma = 0, 0.1 # mean and standard deviation
l = np.random.normal(mu, sigma, (3, 4)) # samples from the "standard normal" distribution
print(l)


# In[17]:


m = np.random.randn(2, 4) # samples from the "standard normal" distribution
print(m)


# See the list of other distributions in: https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.random.html

# # 2. Inspecting Properties:

# In[18]:


a = np.random.randint(0,10, (2,3,4))
print(a)


# In[19]:


a.size


# In[20]:


a.shape


# In[21]:


a.dtype


# In[22]:


b = np.array([1.0, 2.0])
b.dtype


# In[23]:


b_int = b.astype(int)
print(b_int)


# In[24]:


a_list = a.tolist()
print(a_list)


# In[25]:


print(np.asarray(a_list))


# In[26]:


np.info(np.random)


# # 3. Indexing/Slicing/Subsetting

# In[27]:


a = np.random.randint(0,10, (2,3,4))
print(a)


# In[28]:


a[0,0,0]


# In[29]:


a[0][0][0]


# In[30]:


a[1,0,3]


# In[31]:


a[1,1]


# In[32]:


a[:,:,3]


# In[33]:


a[:,0:2,3]


# In[34]:


a[:,:2,3]


# In[35]:


a[:,:2,-1]


# In[36]:


a[:,:2,-2]


# In[37]:


a


# In[38]:


print(a<5)


# In[43]:


print(a<5)


# In[44]:


print(a[a<5])


# In[46]:


a[:,:2,3] = np.zeros((2,2))
a


# # 4. Copying/Sorting/Reshaping

# In[47]:


a = np.array([1,2,3])
b = a
b[0] = 0
a[0] == b[0]


# In[48]:


c = np.copy(a)
c[0] = 5
a[0] == c[0]


# In[49]:


a = np.random.randint(0,10, (3,4))
print(a)


# In[50]:


b = np.sort(a) # sort along the last axis
print(b)


# In[51]:


np.sort(a, axis=0)


# In[52]:


c = a.T
print(c)


# In[53]:


d = a.reshape(2,6)
print(d)


# In[54]:


e = a.flatten()
print(e)


# In[55]:


print(a)


# # 5. Adding/Removing/Combining/Spliting

# In[56]:


a = np.arange(5)
b = np.arange(5,10)
print(a,b)


# In[57]:


c = np.vstack([a,b])
print(c)


# In[58]:


print(np.hstack([a,b]))


# In[59]:


np.delete(c,1,1)


# In[60]:


np.delete(c,1,0)


# In[61]:


print(np.split(c,2))


# See more in: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

# # 6. Math

# ## 6.1 Elementwise

# In[62]:


a = np.arange(0,10).reshape(2,5)
print(a)


# In[63]:


b = np.random.randint(1,10,(2,5))
print(b)


# In[64]:


c = np.add(a, 1)
print(c)


# In[65]:


c = a + 1
print(c)


# In[66]:


d = a - b # np.subtract(a,b)
print(d)


# In[67]:


e = a * b #np.multiply(a,b)
print(e)


# In[68]:


f = a/b # np.divide(a,b)
print(f)


# In[69]:


g = a**b # np.power(a,b)
print(g)


# In[70]:


h = np.sqrt(a)
print(h)


# In[71]:


i = np.sin(a)
print(i)


# For more mathematical functions of NumPy visit: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html

# ## 6.2 Matrix operations

# In[72]:


a = np.array([[1, 0],[1, 1], [0, 1]])
print(a)


# In[73]:


b = np.array([[0, -1], [1, 1]])
print(b)


# Adding and subtracting is the same as prior section.

# In[74]:


np.matmul(a,b)


# In[75]:


np.linalg.inv(b)


# In[76]:


np.linalg.det(b)


# In[77]:


np.trace(b)


# For more information about linear algebra in NumPy see: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html

# ## 7. Statistics

# In[79]:


mu, sigma = 0, 0.1 # mean and standard deviation
a = np.random.normal(mu, sigma, 1000)
b = 3*a+1


# In[80]:


np.mean(a)


# In[81]:


np.median(a)


# In[82]:


np.std(a)


# In[83]:


np.var(a)


# In[84]:


np.cov(np.vstack([a,b])) # compute the covariance matrix of two random variable a and b 


# In[85]:


c = np.array([[1,2],[3,4]])
c


# In[86]:


np.sum(c)


# In[87]:


np.sum(c, axis=1)


# For more statistics in NumPy see: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.statistics.html

# ## 8. Import/Export
# save and load NumPy array in disk:

# In[91]:


np.save('numpy_files/123', np.array([[1, 2, 3], [4, 5, 6]]))


# In[92]:


np.load('numpy_files/123.npy')


# In[93]:


a=np.array([[1, 2, 3], [4, 5, 6]])
b=np.array([1, 2])
np.savez('numpy_files/123.npz', a=a, b=b)
data = np.load('numpy_files/123.npz')
print(data['a'])
print(data['b'])
data.close()


# For more I/O routines: https://docs.scipy.org/doc/numpy/reference/routines.io.html

# Learn more about NumPy: https://docs.scipy.org/doc/numpy/reference/routines.html
