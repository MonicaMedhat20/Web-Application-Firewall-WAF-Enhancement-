import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

#dataset pre-processing realated imports
import sklearn
from urllib.parse import urlparse
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split



#imports related to classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

#READ CSV
fwaf_data=pd.read_csv('payload_full.csv')
print('Done!')

#Data preparation 
n_features=fwaf_data.shape[1] #shape[1] --> no of columns
n_samples =fwaf_data.shape[0] #shape[0] --> no of rows
print("Number of samples:", n_samples) #number of rows in the dataset
print("Number of features:", n_features) #number of columns in the dataset

#printing head and tail of the dataset
print('Head')
fwaf_data.head()
print('Tail')
fwaf_data.tail()

#to determine the datatype for each  column in the dataset
fwaf_data.dtypes

#printing the columns of the dataset
print('Dataset Columns')
fwaf_data.columns

#data visualization
sns.set_style('darkgrid')
sns.countplot(data= fwaf_data, x='label')

#visualizing format
feature_names=[ 'payload', 'length', 'attack_type', 'label']
X=fwaf_data[feature_names]
print(X)

#payload column before transformation
print(X.payload)


#payload column after transformation
X['payload'] = X['payload'].astype(str)
X['payload'] = X['payload'].str.extract(r'(\d+)')
X['payload'] = pd.to_numeric(X['payload'], errors='coerce').fillna(0)
print(X.payload) #payload displayed after being cleaned and converted to numeric payload values

#attack_type column after transformation
X['attack_type'] = X['attack_type'].astype(str)
X['attack_type'] = X['attack_type'].str.extract(r'(\d+)')
X['attack_type'] = pd.to_numeric(X['attack_type'], errors='coerce').fillna(0)
print(X.attack_type) #attack_type displayed after being cleaned and converted to numeric attack_type values



#filtering the length column  based on a condition in which attack_type column is equal to norm
filtered_length = X.loc[X['attack_type'] == 'norm', 'length']
print(filtered_length)



#length column after transformation
X['length'] = X['length'].astype(str)
X['length'] = X['length'].str.extract(r'(\d+)')
X['length'] = pd.to_numeric(X['length'], errors='coerce').fillna(0)
print(X.length) #length displayed after being cleaned and converted to numeric length values



#buidling final dataset to be used for classification
y=X['label']
print(y)

X['label'] = X['label'].astype(str)
X['label'] = X['label'].str.extract(r'(\d+)')
X['label'] = pd.to_numeric(X['label'], errors='coerce').fillna(0)
print(X.label)

labels=['payload', 'length', 'attack_type']
print(X[labels])

print('computing...')
#split dataset in test and train 
x_tr, x_ts, y_tr, y_ts = train_test_split(X[labels], y, test_size=0.3, random_state=0)


print('Done!')

x_tr.head(5)
x_tr.tail(5)


###Random Forest Classifier###
random_forest_model = RandomForestClassifier(random_state=1)
print('Computing....')
# Fit the model
random_forest_model.fit(x_tr,y_tr)
print('Done!')


RT_predictions= random_forest_model.predict(x_ts)

print("Accuracy", accuracy_score(y_ts, RT_predictions))
print("Precision", precision_score(y_ts, RT_predictions, average='weighted', labels=np.unique(RT_predictions)))
print("Recall", recall_score(y_ts, RT_predictions, average='weighted', labels=np.unique(RT_predictions)))
print("F1", f1_score(y_ts, RT_predictions, average='weighted', labels=np.unique(RT_predictions)))
error_rt = (RT_predictions != y_ts).mean()
print("Test error: {:.1%}".format(error_rt))


#generating a model
import pickle

pickle.dump(random_forest_model,open('model2.pkl', '+wb'))
model2 = pickle.load(open('model2.pkl', '+rb'))