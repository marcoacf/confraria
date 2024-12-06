import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import pyodbc
from sqlalchemy import create_engine, inspect, text

# Configurar o layout da página
st.set_page_config(layout="wide")

# pyodbc
engine = create_engine("mssql+pyodbc://scott:tiger@CONSUMER")

# Função transformar query em DataFrame
def sql_df(query):
    with engine.connect() as conexao:
        consulta = conexao.execute(query)
        dados = consulta.fetchall()
    return pd.DataFrame(dados, columns = consulta.keys())

query_migracao = text('''SELECT

SITE,
MES,
CANAL_N0,
CANAL_N2,
CANAL_N4,
COUNT(ACESSO) VOLUME
                      

  FROM [CONSUMER].[CR].[VW_MIGRACAO]
  WHERE MES  BETWEEN '2023-01-01' AND '2023-11-01'

                      GROUP BY
SITE,
MES,
CANAL_N0,
CANAL_N2,
CANAL_N4
                      order by volume desc

''')

df_perfil = sql_df(query_migracao)

# Exibir o DataFrame
st.write(df_perfil)
