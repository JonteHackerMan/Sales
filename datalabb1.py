import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Läser fil skapad i create_sales_data.py
df = pd.read_csv("sales_data.csv")

#Konvertera 'Date' till datetime-format
df['Date'] = pd.to_datetime(df['Date'])

#Ta bort nulls
df = df.dropna()

#Bästsäljare
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("Topp 5 mest sålda produkter:")
print(product_sales.head())

#Försäljning per produkt
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Totalt sålda enheter per produkt")
plt.xlabel("Produkt")
plt.ylabel("Antal sålda enheter")
plt.xticks(rotation=45)
plt.show()

#Försäljning över tid
df['Month'] = df['Date'].dt.to_period('M')  # Extrahera år och månad
monthly_revenue = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line', marker='o')
plt.title("Försäljningsintäkter per månad")
plt.xlabel("Månad")
plt.ylabel("Intäkter (SEK)")
plt.grid(True)
plt.show()

#Försäljning per veckodag
df['Weekday'] = df['Date'].dt.day_name()  # Extrahera veckodag
weekday_revenue = df.groupby('Weekday')['Revenue'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

plt.figure(figsize=(10, 6))
sns.barplot(x=weekday_revenue.index, y=weekday_revenue.values, palette="viridis") #Skippade färg, installera Hue's färgkarta
plt.title("Genomsnittliga intäkter per veckodag")
plt.xlabel("Veckodag")
plt.ylabel("Genomsnittliga intäkter (SEK)")
plt.show()


print("Slutsats:")
print(f"Produkten med högst försäljning är: {product_sales.index[0]}")
print(f"Veckodagen med högst genomsnittlig försäljning är: {weekday_revenue.idxmax()}")