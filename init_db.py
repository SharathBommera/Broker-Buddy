# init_db.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Table, MetaData

# Define database path (make sure 'data/' exists)
engine = create_engine("sqlite:///data/brokerbuddy.db")
metadata = MetaData()

# Define the table schema
properties = Table(
    'properties', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('location', String, nullable=False),
    Column('area_sqft', Float, nullable=False),
    Column('bedrooms', Integer, nullable=False),
    Column('bathrooms', Integer, nullable=False),
    Column('price_lakhs', Float, nullable=False),
    Column('furnish', String, nullable=False),
    Column('property_type', String, nullable=False),
    Column('availability', String, nullable=False)
)

# Create the table
metadata.create_all(engine)

print("Database and 'properties' table created successfully.")
