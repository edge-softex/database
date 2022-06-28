
# --------- DROP TABLES ----------- #
staging_softex_drop = "DROP TABLE IF EXISTS staging_softex"

# --------- CREATE TABLES --------- #

staging_softex_create = ("""CREATE TABLE IF NOT EXISTS staging_softex
                            (
                                staging_softex  SERIAL PRIMARY KEY ,
                                timestamp       varchar            ,
                                radiacao_avg    real               ,
                                temp_cel_avg    real               ,
                                temp_amb_avg    real               ,
                                tensao_s1_avg   real               ,
                                corrent_s1_avg  real               ,
                                potencia_s1_avg real               ,
                                tensao_s2_avg   real               ,
                                corrente_s2_avg real               ,
                                potencia_s2_avg real               ,
                                potencia_fv_avg real               ,
                                demanda_avg     real               ,
                                fp_fv_avg       real               ,
                                tensao_rede_avg real          
                            );
                        """)

# --------- INSERT TABLES --------- #

staging_softex_insert = (""" INSERT INTO staging_softex
                            (
                                timestamp       ,
                                radiacao_avg    ,
                                temp_cel_avg    ,
                                temp_amb_avg    ,
                                tensao_s1_avg   ,
                                corrent_s1_avg  ,
                                potencia_s1_avg ,
                                tensao_s2_avg   ,
                                corrente_s2_avg ,
                                potencia_s2_avg ,
                                potencia_fv_avg ,
                                demanda_avg     ,
                                fp_fv_avg       ,
                                tensao_rede_avg 
                            )
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")
drop_table_queries   = [staging_softex_drop]
create_table_queries = [staging_softex_create]