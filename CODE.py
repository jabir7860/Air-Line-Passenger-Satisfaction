# Importing the modules
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import jovian
%matplotlib inline

raw_df = pd.read_csv('/kaggle/input/airline-passenger-satisfaction/train.csv') # Loading the dataset
raw_df.head()  

raw_df.head().T # Transposing the dataframe for better view 

# Shape of our dataset
raw_df.shap
# Basic infor about dataset
raw_df.info()
# Check for NA or missing values
raw_df.isna().sum()
# Check for number of unique values
raw_df.nunique() 

# Visualisation Setup
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000' 

# How many of each class are there in target column?
raw_df["satisfaction"].value_counts()

fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2, figsize=(15,5))
# Plot 1
ax1.bar(raw_df["satisfaction"].value_counts().index, raw_df["satisfaction"].value_count
ax1.set(title="Satisfaction Distribution",ylabel="Count")
# Plot 2
ax2.pie(raw_df["satisfaction"].value_counts(),colors=["salmon", "lightblue"],
labels= ["Neutral or Dissatisfied", "Satisfied"] ,
autopct='%1.1f%%',explode=[0.05,0.05] ,startangle=0, shadow = True)
ax2.set(title="Satisfaction Distribution") 
        
        
        
        # Sex ratio of Male and Female
raw_df['Gender'].value_counts() 
        
        # Customer Type Ratio
raw_df['Customer Type'].value_counts(
  px.histogram(raw_df,
x='Age',
title='Age vs Satisfaction Ratio',
marginal='box',
color='satisfaction') 
  ============================================================================================================================================
  
  7. Modelling
Now we got our dataset properly preprocessed, splitted into training-validation set and ready for modelling.
# Performing One Hot Encoding
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore').fit(inputs_df[categorica
encoded_cols = list(encoder.get_feature_names(categorical_cols))
inputs_df[encoded_cols] = encoder.transform(inputs_df[categorical_cols])
Gender_Female Gender_Male
Customer
Type_Loyal
Customer
Customer
Type_disloyal
Customer
Type of
Travel_Business
travel
Type of
Travel_Personal
Travel
Class_Business Cla
0 0.0 1.0 1.0 0.0 0.0 1.0 0.0
1 0.0 1.0 0.0 1.0 1.0 0.0 1.0
2 1.0 0.0 1.0 0.0 1.0 0.0 1.0
3 1.0 0.0 1.0 0.0 1.0 0.0 1.0
4 0.0 1.0 1.0 0.0 1.0 0.0 1.0
... ... ... ... ... ... ... ...
103899 1.0 0.0 0.0 1.0 1.0 0.0 0.0
103900 0.0 1.0 1.0 0.0 1.0 0.0 1.0
103901 0.0 1.0 0.0 1.0 1.0 0.0 1.0
103902 1.0 0.0 0.0 1.0 1.0 0.0 0.0
103903 0.0 1.0 1.0 0.0 1.0 0.0 1.0
103904 rows × 9 columns
First we'll try several differernt Classification 
                                                                             Models We'll Try:
1. Logistic Regression
2. Linear SVC
3. K Neighbour Class
4  Navie Bayes
5. Decision Tree
6. Random Forest Class
7. Ada Boost Class
8. XGBoost 
