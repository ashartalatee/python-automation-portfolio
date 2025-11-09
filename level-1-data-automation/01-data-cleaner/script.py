import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Bersihkan nama kolom
    df.columns = df.columns.str.strip()

    # Bersihkan whitespace pada isi cell string
    df = df.applymap(lambda v: v.strip() if isinstance(v, str) else v)

    # Drop baris kosong
    df = df.dropna(how='all')

    # Isi NaN numeric dengan 0
    for col in df.select_dtypes(include=['float', 'int']).columns:
        df[col] = df[col].fillna(0)

    return df
