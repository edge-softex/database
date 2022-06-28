#%%
import psycopg2 as pg
#%%
def create_database():
    """This function is responsible for creates and connects to the 
       softexdb. As also Returns the connection and cursor to 
       softexdb

    Returns:
        tuple[pg.cursor, pg.connection]: cursor and connection to
        softexdb
    """
    #establishing the connection
    conn = pg.connect(
        database="postgres",user='postgres', password='postgres', host='localhost', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor() 

    # create youtube database with UTF8
    cursor.execute("DROP DATABASE IF EXISTS softexdb")
    cursor.execute("CREATE DATABASE softexdb WITH ENCODING 'utf8'")

    conn.close()

    conn = pg.connect(
        database="softexdb",user='postgres', password='postgres', host='localhost', port= '5432'
    )

    cursor = conn.cursor()
    conn.autocommit = True

    # close connection to default database
    return cursor, conn


#%%
def main():
    cur, conn = create_database()

#%%
if __name__ == "__main__":
    main()
# %%
