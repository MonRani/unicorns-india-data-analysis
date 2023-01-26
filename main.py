import pandas as pd
import matplotlib.pyplot as plt

# read in dataset
df = pd.read_csv("dataset.csv")

# rename columns
df.columns = ["No", "Company", "Sector", "Publicly_Listed", "Entry_Valuation_B", "Valuation_B", "Entry", "Former_Unicorn", "Location", "Select_Investors"]

# convert entry and valuation columns to numeric
df["Entry_Valuation_B"] = pd.to_numeric(df["Entry_Valuation_B"])
df["Valuation_B"] = pd.to_numeric(df["Valuation_B"])

# calculate growth as valuation - entry valuation
df["Growth"] = df["Valuation_B"] - df["Entry_Valuation_B"]

# 1) Company Sector popularity in each location
location_sector_counts = df.groupby(["Location", "Sector"]).size().reset_index(name="Counts")
print(location_sector_counts)

# 2) how likely the Select Investors are to invest in each Company Sector
sector_investor_counts = df.groupby(["Sector", "Select_Investors"]).size().reset_index(name="Counts")
print(sector_investor_counts)

# 3) Top 20 Companies with High Growth defined as Valuation ($B) - Entry Valuation($B)
top_20_growth = df.sort_values(by="Growth", ascending=False).head(20)
print(top_20_growth[["Company", "Growth"]])

# 1) Company Sector popularity in each location
location_sector_counts = df.groupby(["Location", "Sector"]).size().reset_index(name="Counts")
location_sector_counts.pivot(index='Location', columns='Sector', values='Counts').plot(kind='bar', stacked=True)
plt.xlabel("Location")
plt.ylabel("Counts")
plt.title("Company Sector Popularity in Each Location")
plt.savefig("location_sector_counts.png")
plt.show()

# 2) how likely the Select Investors are to invest in each Company Sector
sector_investor_counts = df.groupby(["Sector", "Select_Investors"]).size().reset_index(name="Counts")
sector_investor_counts.pivot(index='Sector', columns='Select_Investors', values='Counts').plot(kind='bar', stacked=True)
plt.xlabel("Sector")
plt.ylabel("Counts")
plt.title("Select Investors' Investment in Each Company Sector")
plt.savefig("sector_investor_counts.png")
plt.show()

# 3) Top 20 Companies with High Growth defined as Valuation ($B) - Entry Valuation($B)
top_20_growth = df.sort_values(by="Growth", ascending=False).head(20)
top_20_growth.plot(x="Company", y="Growth", kind="bar")
plt.xlabel("Company")
plt.ylabel("Growth (Valuation - Entry Valuation in $B)")
plt.title("Top 20 Companies with High Growth")
plt.savefig("top_20_growth.png")
plt.show()
