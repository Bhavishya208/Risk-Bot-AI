
import streamlit as st
from src.utils import load_data, risk_label

st.set_page_config(page_title="RiskBot AI", layout="wide")
st.title("📈 RiskBot AI – Financial Risk & Market Insight Dashboard")

df = load_data("data/raw/financial_data.csv")
df["Risk Level"] = df["volatility"].apply(risk_label)

st.metric("Average Volatility", round(df["volatility"].mean(), 4))
st.dataframe(df)
st.bar_chart(df["volatility"])
