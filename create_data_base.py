#%%
import psycopg2 as pg
from sql_queries import create_table_queries, drop_table_queries
from tqdm import tqdm
from sql_queries import *
from utils import *
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


def drop_tables(cur):

    for query in drop_table_queries:
        cur.execute(query)


def create_tables(cur):

    for query in create_table_queries:
        cur.execute(query)


def read_data_base(root_path):

    all_files = get_list_of_files(root_path)

    list_data = [read_dat_file(file) for file in all_files]

    return pd.concat(list_data, ignore_index=True)


def process_softex_data(cur, data_base):
    for index, row in tqdm(data_base.iterrows()):

        softex_data = ( row.TIMESTAMP       ,
                        row.Radiacao_Avg    ,
                        row.Temp_Cel_Avg    ,
                        row.Temp_Amb_Avg    ,
                        row.Tensao_S1_Avg   ,
                        row.Corrente_S1_Avg ,
                        row.Potencia_S1_Avg ,
                        row.Tensao_S2_Avg   ,
                        row.Corrente_S2_Avg ,
                        row.Potencia_S2_Avg ,
                        row.Potencia_FV_Avg ,
                        row.Demanda_Avg     ,
                        row.FP_FV_Avg       ,
                        row.Tensao_Rede_Avg
        )
        cur.execute(staging_softex_insert, softex_data)

#%%
def main():
    cur, conn = create_database()

    drop_tables(cur)
    create_tables(cur)

    softex_database = read_data_base("system_data/")

    process_softex_data(cur,softex_database)

    conn.close()
#%%
if __name__ == "__main__":
    main()
# %%
