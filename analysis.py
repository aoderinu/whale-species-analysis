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
category_counts = df["size_category"].value_counts()
print(category_counts)

# Interpretation
# The most common size cateogry is "medium"
# This suggests that the majority of the whale species in this dataset have average weights
# between 20,000 and 80,000 kg, relecting that dataset's focus on mid - to - large whales 
# rather that the entire range of whale species.

# Visualization 
import matplotlib.pyplot as plt

# Create a bar chart that shows the weight categories and the number of species in each category
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Categories")
plt.ylabel("Counts")
plt.show()