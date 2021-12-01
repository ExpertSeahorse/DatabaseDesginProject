import psycopg2


DB_HOST = "127.0.0.1"
DB_NAME = "FinalProject2"
DB_USER = "David"

def interact(statement):
    conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password="admin123")
    cur = conn.cursor()

    # Execute provided statement
    cur.execute(statement)

    output = cur.fetchall()

    conn.commit()
    cur.close()

    return output
