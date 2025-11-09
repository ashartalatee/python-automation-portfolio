import streamlit as st
import pandas as pd
from script import load_data, calculate_daily_omzet, top_selling_products

st.set_page_config(page_title="Laporan Omzet Harian", layout="wide")
st.title("📊 Laporan Omzet Harian")

uploaded_file = st.file_uploader("Upload file Excel penjualan (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("📋 Data Penjualan")
    st.dataframe(df)

    st.subheader("💰 Omzet Harian")
    omzet = calculate_daily_omzet(df)
    st.line_chart(omzet.set_index('Tanggal')['Total'])

    st.subheader("🏆 Produk Terlaris")
    top_products = top_selling_products(df)
    st.table(top_products)
else:
    st.info("Silakan upload file Excel penjualan untuk melihat laporan.")
