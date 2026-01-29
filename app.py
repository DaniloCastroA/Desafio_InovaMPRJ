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

st.title("Auditoria de Contratos e Pagamentos")

with open("pagamento_acima_do_valor.sql", "r", encoding="utf-8") as file:
    query = file.read()

df = pd.read_sql(query, engine)

df["excedente"] = df["total_pago"] - df["valor_contrato"]
df["ranking_label"] = df["ranking"].astype(str) + "º"

df["label_barra"] = (
    "Contrato " + df["id_contrato"].astype(str) + "<br>" +
    "Valor: R$ " + df["valor_contrato"].map('{:,.2f}'.format) + "<br>" +
    "Excedente: R$ " + df["excedente"].map('{:,.2f}'.format)
)

fig = px.bar(
    df,
    x="ranking_label",
    y="excedente",
    text="label_barra",
    title="Top 10 contratos com maior excedente",
    labels={"ranking_label": "Posição", "excedente": "Excedente (R$)"}
)

st.plotly_chart(fig, use_container_width=True)

with open("pagamentos_sem_notas.sql", "r", encoding="utf-8") as file:
    query = file.read()

df_pagamentos_sem_notas = pd.read_sql(query, engine)

df_pagamentos_sem_notas['fornecedor'] = df_pagamentos_sem_notas['fornecedor'].fillna('Sem fornecedor')

df_agg = df_pagamentos_sem_notas.groupby("fornecedor", as_index=False)["valor"].sum()
df_agg = df_agg.sort_values("valor", ascending=False).head(10)

fig2 = px.bar(
    df_agg,
    x="fornecedor",
    y="valor",
    text=df_agg["valor"].map("R$ {:,.2f}".format),
    title="Top 10 fornecedores com pagamentos sem notas fiscais",
    labels={"valor": "Valor total sem nota (R$)", "fornecedor": "Fornecedor"}
)

fig2.update_traces(hovertemplate=None, textposition="outside")
st.plotly_chart(fig2, use_container_width=True)

with open("contrato_valor_por_dia.sql", "r", encoding="utf-8") as file:
    query = file.read()

df_contrato_valor_por_dia = pd.read_sql(query, engine)
df_contrato_valor_por_dia = df_contrato_valor_por_dia.sort_values("valor_por_dia", ascending=True)

df_contrato_valor_por_dia["valor_contrato"] = pd.to_numeric(df_contrato_valor_por_dia["valor_contrato"], errors='coerce')
df_contrato_valor_por_dia["valor_por_dia"] = pd.to_numeric(df_contrato_valor_por_dia["valor_por_dia"], errors='coerce')

fig3 = px.scatter(
    df_contrato_valor_por_dia,
    x="dias_execucao",
    y="valor_contrato",
    size="valor_contrato",      
    color="fornecedor",         
    hover_name="id_contrato",    
    hover_data={
        "fornecedor": True,
        "dias_execucao": True,
        "valor_contrato": ':.2f',
        "valor_por_dia": ':.2f'
    },
    title="Contratos: Valor vs Tempo de Execução",
    labels={
        "dias_execucao": "Duração (dias)", 
        "valor_contrato": "Valor do contrato (R$)", 
        "valor_por_dia": "Valor por dia"
    }
)

st.plotly_chart(fig3, use_container_width=True)