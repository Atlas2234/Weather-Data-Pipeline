import psycopg2

# Get the connection string of the cloud database
connection_string = "postgresql://Weather_owner:1hRxBuzOP3vr@ep-weathered-boat-a887jtki.eastus2.azure.neon.tech/Weather?sslmode=require"

def connect_to_database():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

    except Exception as e:
        print(f"Error connecting to the database: {e}")