#!/usr/bin/env python
# coding: utf-8

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[2]:


df = pd.read_csv("KNN_Project_Data")


# **Check the head of the dataframe.**

# In[3]:


df.head()


# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[4]:


sns.pairplot(df, hue = "TARGET CLASS")


# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[5]:


from sklearn.preprocessing import StandardScaler


# ** Create a StandardScaler() object called scaler.**

# In[6]:


scaler = StandardScaler()


# ** Fit scaler to the features.**

# In[78]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# **Use the .transform() method to transform the features to a scaled version.**

# In[79]:


scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))


# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[80]:


scaled_df = pd.DataFrame(scaled_features, columns = df.columns[:-1])
scaled_df.head()


# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[81]:


from sklearn.model_selection import train_test_split


# In[82]:


X = scaled_df
y = df["TARGET CLASS"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[83]:


from sklearn.neighbors import KNeighborsClassifier


# **Create a KNN model instance with n_neighbors=1**

# In[84]:


knn = KNeighborsClassifier(n_neighbors=1)


# **Fit this KNN model to the training data.**

# In[85]:


knn.fit(X_train, y_train)


# # Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[86]:


predictions = knn.predict(X_test)


# ** Create a confusion matrix and classification report.**

# In[87]:


from sklearn.metrics import classification_report,confusion_matrix


# In[88]:


print(confusion_matrix(y_test, predictions))
print('\n')
print(classification_report(y_test, predictions))
print('\n')


# In[ ]:





# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# In[103]:



# My version:

k = 0;
error_rate = []
condition = True
while condition : 
    k = k + 1
    knn = KNeighborsClassifier(n_neighbors= k)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    if float(classification_report(y_test, pred_i).split()[25]) > 0.83:
        condition = False
    error_rate.append(np.mean(pred_i != y_test))

print(" with k = ", k)
print('\n')
print(confusion_matrix(y_test, pred_i))
print('\n')
print(classification_report(y_test, pred_i))


# **Now create the following plot using the information from your for loop.**

# In[105]:


#Solution:

error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))



sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
plt.plot(range(1, 40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# In[20]:





# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[21]:


#deja fait

