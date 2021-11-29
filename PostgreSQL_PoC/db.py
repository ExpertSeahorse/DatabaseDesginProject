from db_config import *
import psycopg2


def interact(statement):
    conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER)
    cur = conn.cursor()

    # Execute provided statement
    cur.execute(statement)

    output = cur.fetchall()

    conn.commit()
    cur.close()

    return output



# Create table test
# interact("CREATE TABLE FromPython (idpk SERIAL PRIMARY KEY, something VARCHAR);")