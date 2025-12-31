# Adekunbi Oderinu 
# 12 - 29 - 25

import pandas as pd

# Load the dataset
df = pd.read_csv("data/whales.csv")
 
print(df.head(7))
print(df.info()) 

def categories(weight):
    if weight < 20000:
        category = "Light" 
    elif weight > 80000:
        category = "Heavy"
    else:
        category = "Medium"
    return category

print(categories(1000))

df["size_category"]=df["avg_weight_kg"].apply(categories)
print(df)
print(df["size_category"].value_counts())