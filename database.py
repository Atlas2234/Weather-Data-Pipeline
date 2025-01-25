import psycopg2

# Get the connection string of the cloud database
connection_string = "postgresql://Weather_owner:1hRxBuzOP3vr@ep-weathered-boat-a887jtki.eastus2.azure.neon.tech/Weather?sslmode=require"



def insert_to_database(raw_data):
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Create command to insert weather data into the raw data table on the cloud database
        for entry in raw_data:
            # SQL query with %s placeholders for parameterized queries
            query = "INSERT INTO raw_data(city, weather, temperature, feels_like, max_temp, min_temp, humidity, wind_speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            
            # Data to be inserted into the parameters of the SQL query
            data = (entry["name"], entry["weather"], entry["temperature"], entry["feels"], entry["max_temp"], entry["min_temp"], entry["humidity"], entry["wind_speed"])
            
            # Execute the query with the data
            cursor.execute(query, data)

            # Commit the changes
            conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_top_temp():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM top_temperature;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_city_weather():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM weather;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_max_temp():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM top_max_temperature;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_min_temp():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM low_min_temperature;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_humidity():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM humidity;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")


def fetch_top_wind_speeds():
    try:
        # Connect to the Neon database using the connection string
        conn = psycopg2.connect(connection_string)
        print("Connected to the database successfully")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # SQL query
        select_query = "SELECT * FROM top_wind_speeds;"
        cursor.execute(select_query)

        # Fetch rows from query result
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        for row in rows:
            print(row)

        return rows
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")