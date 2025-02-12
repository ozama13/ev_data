import pandas as pd
from sqlalchemy import create_engine, text

# ✅ Replace with your actual AWS RDS credentials
USERNAME = "postgres"  
PASSWORD = "qaqqaj-ciwHep-4dossi"  
HOST = "portfolio-database.choaewgk228h.us-east-1.rds.amazonaws.com"  
PORT = "5432"  
DATABASE = "postgres"  # ✅ Use the actual database name

# ✅ Create database connection
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define SQL Queries

queries = {
    "Select All Data from EV Table": """
        SELECT * FROM ev_registration;
    """,
    
    "Get EV Data for a Specific State": """
        SELECT * 
        FROM ev_registration
        WHERE state = 'California';
    """,
    
    "Get the Total Number of EVs by State": """
        SELECT state, SUM(ev_total) AS total_evs
        FROM ev_registration
        GROUP BY state
        ORDER BY total_evs DESC;
    """,
    
    "Get the Percentage of EVs by State": """
        SELECT state, 
               (SUM(ev_total) / SUM(total_vehicles)) * 100 AS percent_evs
        FROM ev_registration
        GROUP BY state
        ORDER BY percent_evs DESC;
    """,
    
    "Find the Year with the Highest Number of EVs in a State": """
        SELECT year, SUM(ev_total) AS total_evs
        FROM ev_registration
        WHERE state = 'California'
        GROUP BY year
        ORDER BY total_evs DESC
        LIMIT 1;
    """,
    
    "Get the Top 5 Counties with the Most EVs": """
        SELECT county, SUM(ev_total) AS total_evs
        FROM ev_registration
        GROUP BY county
        ORDER BY total_evs DESC
        LIMIT 5;
    """,
    
    "Compare EV Counts for BEVs and PHEVs": """
        SELECT state, 
               SUM(bev_count) AS bev_count,
               SUM(phev_count) AS phev_count
        FROM ev_registration
        GROUP BY state
        ORDER BY bev_count DESC;
    """,
    
    "Find States with the Largest Discrepancies Between Calculated and Reported EV Percentages": """
        SELECT state,
               percent_ev AS reported_percent,
               (SUM(ev_total) / SUM(total_vehicles)) * 100 AS calculated_percent,
               ABS(percent_ev - ((SUM(ev_total) / SUM(total_vehicles)) * 100)) AS percent_difference
        FROM ev_registration
        GROUP BY state
        HAVING ABS(percent_ev - ((SUM(ev_total) / SUM(total_vehicles)) * 100)) > 0.1
        ORDER BY percent_difference DESC;
    """,
    
    "Get Average EV Percentage by Year": """
        SELECT year, 
               AVG(percent_ev) AS avg_percent_ev
        FROM ev_registration
        GROUP BY year
        ORDER BY year DESC;
    """,
    
    "Get the Total Number of EVs for a Specific Year": """
        SELECT SUM(ev_total) AS total_evs
        FROM ev_registration
        WHERE year = 2020;
    """,
    
    "Get the Total EV Count by Primary Use (BEVs and PHEVs)": """
        SELECT vehicle_primary_use, 
               SUM(bev_count) AS bev_count,
               SUM(phev_count) AS phev_count
        FROM ev_registration
        GROUP BY vehicle_primary_use
        ORDER BY bev_count DESC;
    """,
    
    "Find the Top 10 Counties with the Highest Percent of EVs": """
        SELECT county, 
               (SUM(ev_total) / SUM(total_vehicles)) * 100 AS percent_evs
        FROM ev_registration
        GROUP BY county
        ORDER BY percent_evs DESC
        LIMIT 10;
    """,
    
    "Calculate the Total Number of Vehicles by Year": """
        SELECT year, SUM(total_vehicles) AS total_vehicles
        FROM ev_registration
        GROUP BY year
        ORDER BY year DESC;
    """,
    
    "Get the Number of EVs by State and County": """
        SELECT state, county, SUM(ev_total) AS total_evs
        FROM ev_registration
        GROUP BY state, county
        ORDER BY total_evs DESC;
    """,
    
    "Identify Years with Low EV Adoption": """
        SELECT year, 
               (SUM(ev_total) / SUM(total_vehicles)) * 100 AS percent_evs
        FROM ev_registration
        GROUP BY year
        HAVING (SUM(ev_total) / SUM(total_vehicles)) * 100 < 5
        ORDER BY year DESC;
    """
}

# Execute Queries and Print Results
for query_name, query in queries.items():
    try:
        print(f"\nExecuting Query: {query_name}")
        with engine.connect() as conn:
            result = conn.execute(text(query))
            # If the result is a query that returns rows (like SELECT), fetch and print the results
            if result.returns_rows:
                rows = result.fetchall()
                for row in rows:
                    print(row)
            else:
                print("Query executed successfully, no rows returned.")
    except Exception as e:
        print(f"❌ Error executing {query_name}: {e}")

