import streamlit as st
import pandas as pd
from script import clean_dataframe

st.title("Data Cleaner Otomatis")

uploaded_file = st.file_uploader("Upload file Excel atau CSV", type=["xlsx", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Sebelum")
    st.dataframe(df)

    cleaned = clean_dataframe(df)
    st.subheader("Sesudah")
    st.dataframe(cleaned)

    st.download_button("Download Hasil", cleaned.to_csv(index=False), "cleaned.csv", "text/csv")
