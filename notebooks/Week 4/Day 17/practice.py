import os
import pandas as pd
import numpy as np
import seaborn as sns


print(os.getcwd())

df_tips = sns.load_dataset("tips")
# df_tips = pd.read_csv("tips")
# print (df_tips.head())

# df_penguins = sns.load_dataset("penguins")
# print (df_penguins.head())

# df_diamonds = sns.load_dataset("diamonds")
# print (df_diamonds.head())

# df_tips = df_tips.rename( columns = {"sex":"gender"})
# print ("updated tips", df_tips.head())
    
# print ("Shape" , df_tips.shape)
# print ("information", df_tips.info)
print (df_tips.describe())
print (df_tips.info())







