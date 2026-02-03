
# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the Given CSV File
df = pd.read_csv(r"C:\Users\Omkar\OneDrive\Desktop\oasis projects\CleaningData\AB_NYC_2019.csv")


# 3. Initial Data Inspection
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 4. Handling Missing Values
df['reviews_per_month'].fillna(0, inplace=True)
df['last_review'].fillna("No Review", inplace=True)
df['name'].fillna("Unknown", inplace=True)
df['host_name'].fillna("Unknown", inplace=True)

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# 5. Remove Duplicate Rows
duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicate_count)

df.drop_duplicates(inplace=True)

# 6. Standardization
# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Remove invalid prices (price <= 0)
df = df[df['price'] > 0]

# 7. Outlier Detection (Price)
plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'])
plt.title("Price Distribution Before Outlier Removal")
plt.show()

# Remove extreme outliers
df = df[df['price'] <= 1000]

plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'])
plt.title("Price Distribution After Outlier Removal")
plt.show()

# 8. Final Dataset Summary
print("\nFinal Dataset Info:")
print(df.info())

print("\nFinal Dataset Shape:", df.shape)

# 9. Save the Cleaned Dataset
df.to_csv("AB_NYC_2019_CLEANED.csv", index=False)

print("\n Data Cleaning Completed Successfully!")
print(" Cleaned file saved as: AB_NYC_2019_CLEANED.csv")
