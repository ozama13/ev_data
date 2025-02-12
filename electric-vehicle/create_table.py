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

# ✅ SQL query to create the table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ev_registration (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    county VARCHAR(255) NOT NULL,
    state VARCHAR(50) NOT NULL,
    vehicle_primary_use VARCHAR(100),
    bev_count INTEGER,
    phev_count INTEGER,
    ev_total INTEGER,
    non_ev_total INTEGER,
    total_vehicles INTEGER,
    percent_ev FLOAT
);
"""

# ✅ Execute the query
try:
    with engine.connect() as conn:
        conn.execute(text(CREATE_TABLE_QUERY))
        print("✅ Table 'ev_registration' created successfully!")
except Exception as e:
    print(f"❌ Table creation failed: {e}")
