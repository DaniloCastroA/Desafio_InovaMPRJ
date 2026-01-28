import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import plotly.express as px

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

df["excedente"] = df["total_pago"] - df["valor_contrato"]
df["data"] = pd.to_datetime(df["data"])

fig = px.bar(
    df,
    x="data",                  
    y="excedente",             
    title="Excedente de pagamento por contrato ao longo do tempo",
    labels={
        "data": "Data do contrato",
        "excedente": "Excedente (R$)"
    },
    hover_data={
        "valor_contrato": True,
        "total_pago": True,
        "excedente": True,
        "id_contrato": True
    }
)

st.plotly_chart(fig, use_container_width=True)