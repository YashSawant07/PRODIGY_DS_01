import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\YASH\Desktop\API_SP.POP.TOTL_DS2_en_csv_v2_85\API_SP.POP.TOTL_DS2_en_csv_v2_85.csv", skiprows=4)

# Filter out unnecessary columns
df = df[['Country Name', '2022']]
print(df)

# Drop rows with missing values
df = df.dropna()

# Sort the DataFrame by population in descending order
df = df.sort_values(by='2022', ascending=False)
print(df)

# Take top 10 countries for visualization
top_10_countries = df.head(10)

# Create bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries['Country Name'], top_10_countries['2022'], color='skyblue')
plt.title('Top 10 Countries by Population in 2022')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()