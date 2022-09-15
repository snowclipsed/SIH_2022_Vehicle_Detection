#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


pip install tf2-yolov4


# In[3]:


pip install -r requirements.txt


# In[4]:


import cv2


# In[5]:


import numpy as np


# In[6]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.imshow(mpimg.imread('test_images/imtest1.jpeg'))


# In[7]:


get_ipython().run_line_magic('run', 'detect.py --weights runs/train/exp12/weights/best.pt --source test_images/imtest13.JPG')


# In[8]:


get_ipython().run_line_magic('run', 'detect.py --weights runs/train/exp12/weights/best.pt --source test_images/v1.MP4')


# In[12]:


get_ipython().run_line_magic('run', 'detect.py --weights runs/train/exp12/weights/best.pt --source test_images/testnet1.JPG')


# In[ ]:




