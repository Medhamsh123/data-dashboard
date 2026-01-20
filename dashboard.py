import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sample_data.csv")

# Create line chart
plt.figure()
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=30)

# Save chart
plt.savefig("sales_chart.png")
plt.show()
