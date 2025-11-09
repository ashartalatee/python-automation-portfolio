import streamlit as st
from script import merge_excels, save_merged

st.title("📊 Merge Multiple Excel Files")

uploaded_files = st.file_uploader(
    "Pilih beberapa file Excel untuk digabungkan", 
    type=["xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    # Simpan sementara file yang diupload
    file_paths = []
    for uploaded_file in uploaded_files:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
            file_paths.append(uploaded_file.name)
    
    st.success(f"{len(uploaded_files)} file siap digabungkan!")
    
    if st.button("Gabungkan Data"):
        merged_df = merge_excels(file_paths)
        st.dataframe(merged_df)  # Preview hasil
        output_file = save_merged(merged_df)
        st.success(f"File berhasil digabungkan dan disimpan → {output_file}")
        st.download_button(
            label="Download Merged Excel",
            data=open(output_file, "rb").read(),
            file_name="merged.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
