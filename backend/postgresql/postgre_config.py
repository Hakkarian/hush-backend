import psycopg2

def configure_postgresql():
    # Configure PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="$=w_$%v7M=`|;[n92}$YJ$8XGTk_hfz6!",
        port=5433
    )
    cursor = conn.cursor()

    # Create a table to store pictures
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pictures (
            id SERIAL PRIMARY KEY,
            cloudinary_id VARCHAR(255),
            cloudinary_url VARCHAR(255)
        )
    """)

    return conn, cursor