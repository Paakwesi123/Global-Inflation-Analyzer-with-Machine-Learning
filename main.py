import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# ================================
# Load and Clean the Dataset
# ================================

# Load Data
df = pd.read_csv("data/global_inflation_data.csv")

# Melt year columns into rows
df_melted = df.melt(id_vars=["country_name"],
                    value_vars=[str(y) for y in range(1980, 2025)],
                    var_name="year", value_name="inflation")

# Drop rows with missing inflation values
df_melted.dropna(subset=["inflation"], inplace=True)

# Convert year to int
df_melted["year"] = df_melted["year"].astype(int)

# Preview cleaned data
print("Cleaned DataFrame:")
print(df_melted.head())

# ================================
# Exploratory Data Analysis (EDA)
# ================================

# Plot inflation trends for selected countries
selected_countries = ["United States", "Ghana", "Germany", "Argentina", "Japan"]
plt.figure(figsize=(12, 6))
for country in selected_countries:
    subset = df_melted[df_melted["country_name"] == country]
    plt.plot(subset["year"], subset["inflation"], label=country)
plt.title("Inflation Trend (1980–2024)")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("inflation_trends.png")
plt.close()

# ================================
# Machine Learning – Predict Future Inflation for Ghana
# ================================

# Prepare data for ML
country = "Ghana"
ghana_data = df_melted[df_melted["country_name"] == country]
X = ghana_data[["year"]]
y = ghana_data["inflation"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, predictions))
print(f"\nModel RMSE for {country}: {rmse:.2f}")

# Predict future years
future_years = pd.DataFrame({"year": list(range(2025, 2030))})
future_predictions = model.predict(future_years)

# Show future predictions
print("\nPredicted Inflation for Ghana (2025–2029):")
for year, rate in zip(future_years["year"], future_predictions):
    print(f"{year}: {rate:.2f}%")

# Save to CSV
pred_df = pd.DataFrame({"year": future_years["year"], "predicted_inflation": future_predictions})
pred_df.to_csv("ghana_inflation_predictions.csv", index=False)

print("\nDone. Check the folder for saved chart and prediction file.")
