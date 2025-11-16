#MapPlot.py
#Name:Bennett Schulte
#Date:11/15/25
#Assignment:Lab 10


import matplotlib.pyplot as plt
import pandas as pd
import cars   


raw_data = cars.get_car()   


df = pd.json_normalize(raw_data)

print("\nFirst 5 rows:\n")
print(df.head())

print("\nColumn names:\n")
print(df.columns)


df = df[["Fuel Information.City mpg", "Engine Information.Engine Statistics.Horsepower", "Dimensions.Length"]]

df = df.dropna()


df.columns = ["MPG", "Horsepower", "Length"]




plt.figure(figsize=(8, 5))
plt.hist(df["MPG"], bins=20)
plt.title("Distribution of City MPG")
plt.xlabel("MPG")
plt.ylabel("Number of Cars")
plt.savefig("mpg_histogram.png") 
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Length"], df["Horsepower"])
plt.title("Horsepower vs Car Length")
plt.xlabel("Length (inches)")
plt.ylabel("Horsepower")
plt.savefig("hp_vs_length_scatter.png")   
plt.show()

print("\nPlots created and saved successfully!\n")
