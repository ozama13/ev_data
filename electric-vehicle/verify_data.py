from sqlalchemy import create_engine, text

# Database credentials
USERNAME = "postgres"
PASSWORD = "qaqqaj-ciwHep-4dossi"
HOST = "portfolio-database.choaewgk228h.us-east-1.rds.amazonaws.com"
PORT = "5432"
DATABASE = "postgres"

# ✅ Create database connection string
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

# ✅ Fetch the first 5 rows from the database
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM ev_registration LIMIT 5;"))
        for row in result:
            print(row)
except Exception as e:
    print(f"❌ Query failed: {e}")
