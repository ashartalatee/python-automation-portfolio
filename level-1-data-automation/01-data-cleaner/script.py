import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Membersihkan dataframe:
    - Trim whitespace di kolom dan string
    - Drop row kosong
    - Fill NaN numerik dengan 0
    """
    df = df.copy()
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda v: v.strip() if isinstance(v, str) else v)
    df = df.dropna(how='all')
    
    for col in df.select_dtypes(include=['float', 'int']).columns:
        df[col] = df[col].fillna(0)
    
    return df
