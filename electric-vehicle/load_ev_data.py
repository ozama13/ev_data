import pandas as pd
from sqlalchemy import create_engine

# ✅ Replace with your actual AWS RDS credentials
# Database credentials
USERNAME = "postgres"
PASSWORD = "qaqqaj-ciwHep-4dossi"
HOST = "portfolio-database.choaewgk228h.us-east-1.rds.amazonaws.com"
PORT = "5432"
DATABASE = "postgres"

# ✅ Create database connection string
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

# ✅ Load cleaned CSV data
file_path = "cleaned_electric_vehicle.csv"  # Make sure this file is in the same directory
df = pd.read_csv(file_path)

# ✅ Rename columns to match table schema
df.columns = ["date", "county", "state", "vehicle_primary_use", "bev_count", "phev_count",
              "ev_total", "non_ev_total", "total_vehicles", "percent_ev", "year", "month"]

# ✅ Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# ✅ Load data into PostgreSQL
try:
    df.to_sql("ev_registration", engine, if_exists="append", index=False)
    print("✅ EV dataset loaded into RDS successfully!")
except Exception as e:
    print(f"❌ Data loading failed: {e}")