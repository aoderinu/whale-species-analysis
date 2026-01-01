# Adekunbi Oderinu 
# 12 - 29 - 25

import pandas as pd

# Load the dataset
df = pd.read_csv("data/whales.csv")
 
print(df.head(7))
print(df.info()) 

# Create a function that uses the average weights to categorize the whale species 
def categories(weight):
    if weight < 20000:
        category = "Light" 
    elif weight > 80000:
        category = "Heavy"
    else:
        category = "Medium"
    return category

print(categories(1000))

# Create a new collumn in the data frame that lists the categories using the .apply() function
df["size_category"] = df["avg_weight_kg"].apply(categories)
print(df)

# Count how many whale species are in each category using .value_counts()
print(df["size_category"].value_counts())