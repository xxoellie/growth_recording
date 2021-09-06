#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
print(os.getcwd())


# In[ ]:


import tensorflow as tf
import numpy as np
import pandas as pd
import os 

import matplotlib.pyplot as plt 
from PIL import Image


# In[3]:


img = Image.open(r"Study\딥러닝\flowers\sunflower\6953297_8576bf4ea3.jpg")
print("img : \n", img)


# In[4]:


plt.imshow(img)
plt.show()


# In[5]:


img_array = np.array(img)
print(img_array.shape)
print(img_array)


# In[6]:


resized = img.resize([100,100])
print(resized)
plt.imshow(resized)
plt.show()

resized_array = np.array(resized)
print(resized_array.shape)


# In[7]:


print(os.getcwd())


# In[8]:


path = 'Study/딥러닝/flowers/'
filenames = os.listdir(path)
print(filenames)


# In[9]:


def list_dir(path):
    filesnames = os.listdir(path)
    filesnames.sort()
    return filesnames


# In[10]:


target_names = list_dir(path=path)
print(target_names)


# In[11]:


for dx, dname in enumerate(target_names):
    print(dname)
    
    subpath = path + dname
    print(subpath)
    
    filenames = list_dir(path=subpath)
    print(filenames[:3])


# In[12]:


imagepath = os.path.join(subpath, filenames[2])
print("imagepath : ", imagepath)


# In[13]:


img = Image.open(imagepath)
img


# In[14]:


resize = img.resize([100,100])
resize_np_array = np.array(resize)
print("resize_np_array.shape : \n", resize_np_array.shape)


# In[15]:


def load_image_pixels(imagepath, resolution):
    img = Image.open(imagepath)
    img_resize = img.resize(resolution)
    
    return np.array(img_resize)


# In[16]:


resolution = [100,100]
pixels = load_image_pixels(imagepath = imagepath, 
                           resolution = resolution)
print("pixels : \n", pixels)


# In[17]:


resolution = [100,100]

def flowers_init(resolution):
    path = 'Study/딥러닝/flowers/'
    target_names = list_dir(path)
    
    images = []
    idxs   = []
    
    for dx, dname in enumerate(target_names):
        print("dname : ", dname)
        
        subpath = path + dname
        print("subpath : ", subpath)
        
        filenames = list_dir(subpath)
        print("filenames : ", filenames[:3])
        
        for fname in filenames:
            
            if fname[-4:] != '.jpg':
                continue
            
            imagepath = os.path.join(subpath, fname)
            
            pixels = load_image_pixels(imagepath, resolution)
            
            images.append(pixels)
            idxs.append(dx)
            
    xs = np.asarray(images, dtype=np.float32)
    
    return xs, images, idxs  


# In[18]:


xs, images, idxs = flowers_init(resolution = resolution)


# In[19]:


print(xs.shape)


# In[20]:


pd.DataFrame(idxs).value_counts()


# In[21]:


img = xs[11]

img_image = Image.fromarray(np.uint8(img))
plt.imshow(img_image)
plt.show()


# In[23]:


plt.figure(figsize=(15,15))

for i in range(16):
    plt.subplot(4,4,i+1)
    i   = np.random.choice(4317)
    img = xs[i]
    img_image = Image.fromarray(np.uint8(img))
    plt.axis('off')
    plt.imshow(img_image)
    
plt.show()


# In[24]:


cnt = 5
np.eye(cnt)


# In[ ]:


idxs


# In[46]:


print(np.eye(cnt)[0])
print(np.eye(cnt)[1])
print(np.eye(cnt)[2])
print(np.eye(cnt)[3])


# In[27]:


def onehot(idxs, cnt):
    return np.eye(cnt)[idxs]


# In[41]:


cnt = len(target_names)
cnt


# In[44]:


ys = onehot(idxs=idxs, cnt = cnt)
print(ys[0])
print(ys[1])
print(ys[2])
print(ys[6])
print(ys[1000])


# In[34]:


def flowers_init(resolution):
    path = 'Study/딥러닝/flowers/'
    target_names = list_dir(path)
    
    images,idxs = [], []
    
    for dx, dname in enumerate(target_names):
        print('dname : ', dname)

        subpath = path + dname
        print("subpath : ", subpath)

        filepath = list_dir(subpath)
        print("filepath : ", filepath[:3])
        
        for fname in filepath:
            if fname[-4:] != '.jpg':
                continue
            imagepath = os.path.join(subpath, fname)
            
            pixels = load_image_pixels(imagepath, resolution)
            
            images.append(pixels)
            idxs.append(dx)
            
    xs = np.asarray(images, dtype=np.float32)
    
    ys = onehot(idxs=idxs, cnt = len(target_names))
    
    return xs, ys


# In[35]:


xs, ys = flowers_init(resolution = [100,100])


# In[48]:


xs


# In[36]:


print("xs.shape : ", xs.shape)
print("ys.shape : ", ys.shape)


# In[37]:


plt.figure(figsize=(12,12))

for i in range(16):
    plt.subplot(4,4,i+1)
    i   = np.random.choice(4317)
    img = xs[i]
    img_image = Image.fromarray(np.uint8(img))
    
    plt.title("test_y_onehot :\n{}".format(ys[i]))
    
    plt.axis('off')
    plt.imshow(img_image)
    
plt.show()


# In[47]:


print("xs.max() : ", xs.max())
print("xs.min() : ", xs.min())


# In[49]:


xs_norm = xs / 255.0
print("xs_norm.max() : ", xs_norm.max())
print("xs_norm.min() : ", xs_norm.min())


# In[52]:


print(xs_norm.shape)
shuffle_map = np.arange(xs_norm.shape[0])
np.random.shuffle(shuffle_map)
print("shuffle_map : \n ",shuffle_map)


# In[53]:


train_ratio = 0.8

test_begin_index = int(xs_norm.shape[0] * train_ratio)
print("test_begin_index : ", test_begin_index)


# In[54]:


train_x = xs[shuffle_map[:test_begin_index]]
test_x  = xs[shuffle_map[test_begin_index:]]

train_y = ys[shuffle_map[:test_begin_index]]
test_y  = ys[shuffle_map[test_begin_index:]]


# In[55]:


print("train_x.shape : ", train_x.shape)
print("train_y.shape : ", train_y.shape)
print("test_x.shape : ", test_x.shape)
print("test_y.shape : ", test_y.shape)


# In[56]:


plt.figure(figsize=(12,12))

for i in range(36):
    plt.subplot(6,6,i+1)
    i   = np.random.choice(3453)
    img = train_x[i]
    img_image = Image.fromarray(np.uint8(img))
    
    plt.title("test_y_onehot :\n{}".format(train_y[i]))
    
    plt.axis('off')
    plt.imshow(img_image)
    
plt.show()


# In[57]:


model_1 = tf.keras.Sequential([
    tf.keras.layers.Conv2D(input_shape=(100,100,3),kernel_size=(3,3),filters=32),
    tf.keras.layers.MaxPool2D(strides = (2,2),pool_size=(2,2)),
    tf.keras.layers.Conv2D(kernel_size=(3,3),filters = 64),
    tf.keras.layers.AvgPool2D(strides = (2,2)),
    tf.keras.layers.Conv2D(kernel_size=(3,3),filters=128),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=128, activation = 'relu'),
    tf.keras.layers.Dropout(rate = 0.3),
    tf.keras.layers.Dense(units=5, activation = 'softmax')
])


# In[58]:


model_1.summary()


# In[59]:


model_1.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.00001),
               loss       = 'categorical_crossentropy',
               metrics    = [tf.keras.metrics.TruePositives(name = 'True_positives'),
                            tf.keras.metrics.FalsePositives(name = 'False_positives')])


# In[60]:


history = model_1.fit(train_x, train_y,
                     epochs           = 50,
                     validation_split = 0.2,
                     batch_size       = 32)


# In[61]:


model_1.save('flowers_model_1.h5')


# In[97]:


model_1.evaluate(test_x, test_y)


# In[98]:


pred_y = model_1.predict(test_x)


# In[99]:


print(np.round(pred_y, 3))


# In[100]:


pred_y.shape


# In[101]:


# 테스트 데이터 12번째 
test_index = 17
# 예측 값 중에서 가장큰 인덱스를 출력 (예측 값)
print("pred_y_{} -> {}".format(test_index, np.argmax(pred_y[test_index])))
# 테스트 데이터의 확률분포 중 가장 큰 값을 출력(실제 값) 
print("test_y_{} -> {}".format(test_index, np.argmax(test_y[test_index])))
print("Prob : ",np.round(pred_y[test_index],3))

img = test_x[test_index]
img_image = Image.fromarray(np.uint8(img))
plt.imshow(img_image)
plt.axis('off')
plt.show()


# In[103]:


plt.figure(figsize=(20,20))

for i in range(16):
    
    plt.subplot(4,4,i+1)
    
    i = np.random.choice(864)
    img = test_x[i]
    img_Image = Image.fromarray(np.uint8(img))
    plt.imshow(img_Image)
    
    plt.title('pred_y : {} , test_y : {} \nProb : {}'.format(np.argmax(pred_y[i]), np.argmax(test_y[i]), np.round(pred_y[i],3)))
    plt.axis('off')

plt.draw()


# In[1]:


pip install jupytext


# In[ ]:




