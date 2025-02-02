import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
     

plt.hist(dataset, bins=50)
plt.show()

#z-score
outliers=[]
def detect_outliers(data):
    
    threshold=3
    mean = np.mean(data)
    std =np.std(data)
    
    
    for i in data:
        z_score= (i - mean)/std 
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

outlier_pt=detect_outliers(dataset)

outlier_pt

"""IQR
Sort the data
Calculate Q1 aqnd Q3
IQR(Q3-Q1)
Find the Lower fence(q1-1.5(iqr))
Find the upper fence(q3+1.5(iqr))"""

dataset=sorted(dataset)
dataset

quantile1, quantile3= np.percentile(dataset,[25,75])

print(quantile1,quantile3)

iqr_value=quantile3-quantile1

print(iqr_value)

lower_bound_val = quantile1 -(1.5 * iqr_value)
upper_bound_val = quantile3 +(1.5 * iqr_value)

print(lower_bound_val,upper_bound_val)

sns.boxplot(dataset)