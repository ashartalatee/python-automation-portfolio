import streamlit as st
import pandas as pd
from script import generate_report, send_report

st.set_page_config(page_title="Kirim Laporan Otomatis", page_icon="📤", layout="centered")
st.title("📤 Kirim Laporan Otomatis")
st.markdown("Upload file Excel berisi data penjualan hari ini:")

uploaded_file = st.file_uploader("Pilih file Excel", type=["xlsx"])

if uploaded_file:
    st.success("File berhasil diupload ✅")
    
    df = pd.read_excel(uploaded_file)
    st.subheader("Preview Data")
    st.dataframe(df.head())

    # Generate Laporan
    if st.button("📊 Generate Laporan"):
        report_file = generate_report(df)
        st.session_state.report_file = report_file
        st.success(f"Laporan berhasil dibuat: {report_file}")
        st.download_button("⬇️ Download Laporan", report_file)

    # Kirim Laporan
    st.subheader("Kirim Laporan")
    recipient = st.text_input("Nomor WA atau Email penerima")

    if st.button("📤 Kirim Laporan"):
        if not recipient:
            st.warning("Isi nomor penerima terlebih dahulu")
        elif 'report_file' not in st.session_state:
            st.warning("Klik dulu 'Generate Laporan' sebelum kirim")
        else:
            result = send_report(st.session_state.report_file, recipient)
            if result:
                st.success(f"Laporan berhasil dikirim ke {recipient} ✅ (disimpan di folder sent_reports)")
            else:
                st.error("Gagal mengirim laporan ❌")
