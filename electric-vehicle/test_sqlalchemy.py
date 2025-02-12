from sqlalchemy import create_engine

# Sample SQLite connection (works without setup)
engine = create_engine("sqlite:///:memory:")
print("SQLAlchemy installed and working!")
