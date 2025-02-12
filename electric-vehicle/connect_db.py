from connect_db import create_engine, text
import pandas as pd

# Database credentials
USERNAME = "postgres"
PASSWORD = "qaqqaj-ciwHep-4dossi"
HOST = "portfolio-database.choaewgk228h.us-east-1.rds.amazonaws.com"
PORT = "5432"
DATABASE = "postgres"

# ✅ Create database connection string
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# ✅ Test connection
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1;"))  # ✅ FIX: Use text()
        print("✅ Connected to AWS RDS PostgreSQL successfully!")
except Exception as e:
    print(f"❌ Connection failed: {e}")



