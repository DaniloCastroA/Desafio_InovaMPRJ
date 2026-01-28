import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

st.set_page_config(page_title="Auditoria de Contratos", layout="wide")

password = urllib.parse.quote_plus("DesafioInov@2026!")

engine = create_engine(
    f"postgresql://candidato.jdazostyahhxukbmxybw:{password}"
    "@aws-1-us-east-1.pooler.supabase.com:5432/postgres"
)

st.title("contratos com pagamento acima do valor contratado")

with open("query.sql", "r", encoding="utf-8") as file:
    query = file.read()

df = pd.read_sql(query, engine)

st.dataframe(df)