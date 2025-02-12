import pandas as pd

# Load CSV File
file_path = "electric-vehicle.csv"  # Update with correct path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%B %d %Y")

# Extract Year and Month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Standardize categorical columns
df['County'] = df['County'].str.strip().str.title()  # Capitalize County
df['State'] = df['State'].str.upper()  # Ensure uppercase state codes
df['Vehicle Primary Use'] = df['Vehicle Primary Use'].str.capitalize()

# Handle missing values
df['County'].fillna("Unknown", inplace=True)
df['State'].fillna("Unknown", inplace=True)

# Ensure numeric columns are correct
numeric_cols = ["Battery Electric Vehicles (BEVs)", "Plug-In Hybrid Electric Vehicles (PHEVs)", 
                "Electric Vehicle (EV) Total", "Non-Electric Vehicle Total", "Total Vehicles", 
                "Percent Electric Vehicles"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Recalculate Percent Electric Vehicles to validate accuracy
df['Recalculated Percent EV'] = (df['Electric Vehicle (EV) Total'] / df['Total Vehicles']) * 100

# Check for inconsistencies
df['Percent Difference'] = df['Percent Electric Vehicles'] - df['Recalculated Percent EV']

# Identify large discrepancies
df_discrepancies = df[df['Percent Difference'].abs() > 0.1]

# Drop the columns 'Recalculated Percent EV' and 'Percent Difference' after calculation
df.drop(['Recalculated Percent EV', 'Percent Difference'], axis=1, inplace=True)

# Save cleaned data
df.to_csv("cleaned_electric_vehicle.csv", index=False)

# Print first few rows
print(df.head())
print("\nDiscrepancies in percentage calculation:\n", df_discrepancies)
