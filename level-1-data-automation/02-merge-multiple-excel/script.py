import pandas as pd
import os

def merge_excels(file_paths):
    """
    Merge beberapa file Excel menjadi satu DataFrame
    :param file_paths: list of string (path ke file Excel)
    :return: pandas DataFrame gabungan
    """
    df_list = []
    for file in file_paths:
        df = pd.read_excel(file)
        df_list.append(df)
    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df

def save_merged(df, output_path="merged.xlsx"):
    """
    Simpan hasil gabungan ke Excel
    """
    df.to_excel(output_path, index=False)
    return output_path
