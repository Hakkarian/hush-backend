import psycopg2

def configure_postgresql():
    # Configure PostgreSQL
    conn = psycopg2.connect(
        host="your_postgresql_host",
        database="postgres",
        user="your_user",
        password="your_password"
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
    conn.commit()

    return conn, cursor