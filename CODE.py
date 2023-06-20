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

#4.2 Visulaistion and Finding Patterns
# Visualisation Setup
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
# How many of each class are there in target column?
raw_df["satisfaction"].value_counts()
neutral or dissatisfied 58879
satisfied 45025
Name: satisfaction, dtype: int64
# Visualising the satisfation distribution among passengers
fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2, figsize=(15,5))
# Plot 1
ax1.bar(raw_df["satisfaction"].value_counts().index, raw_df["satisfaction"].value_count
ax1.set(title="Satisfaction Distribution",ylabel="Count")
# Plot 2
ax2.pie(raw_df["satisfaction"].value_counts(),colors=["salmon", "lightblue"],
labels= ["Neutral or Dissatisfied", "Satisfied"] ,
autopct='%1.1f%%',explode=[0.05,0.05] ,startangle=0, shadow = True)
ax2.set(title="Satisfaction Distribution")
