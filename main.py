import pandas as pd
import matplotlib.pyplot as plt

# read the dataset into a pandas dataframe
df = pd.read_csv("dataset.csv")

# clean the data (if necessary)
df.dropna(inplace=True)

# 1) top 10 Sectors which have the most number of companies
top_sectors = df['Sector'].value_counts().nlargest(10)
print(top_sectors)

# 2) Comparison of Entry Valuation and Valuation of top ten companies with highest valuation
top_valuations = df.nlargest(10, 'Valuation ($B)')
comparison = top_valuations[['Company', 'Entry Valuation($B)', 'Valuation ($B)']]
print(comparison)

# 3) Top 20 Companies with High Growth defined as Valuation ($B) - Entry Valuation($B)
df['Growth'] = df['Valuation ($B)'] - df['Entry Valuation($B)']
top_growth = df.nlargest(20, 'Growth')
top_growth = top_growth[['Company', 'Growth']]
print(top_growth)

# 1) top 10 Sectors which have the most number of companies
top_sectors.plot(kind='bar')
plt.xlabel('Sector')
plt.ylabel('Number of Companies')
plt.title('Top 10 Sectors with the Most Number of Companies')
plt.savefig('top_sectors.png')
plt.show()

# 2) Comparison of Entry Valuation and Valuation of top ten companies with highest valuation
comparison.plot(x='Company', y=['Entry Valuation($B)', 'Valuation ($B)'], kind='bar')
plt.xlabel('Company')
plt.ylabel('Valuation ($B)')
plt.title('Comparison of Entry Valuation and Valuation of Top Ten Companies with Highest Valuation')
plt.legend(['Entry Valuation', 'Valuation'])
plt.savefig('valuation_comparison.png')
plt.show()

# 3) Top 20 Companies with High Growth defined as Valuation ($B) - Entry Valuation($B)
top_growth.plot(x='Company', y='Growth', kind='bar')
plt.xlabel('Company')
plt.ylabel('Growth (Valuation ($B) - Entry Valuation($B))')
plt.title('Top 20 Companies with High Growth')
plt.savefig('top_growth.png')
plt.show()
