import pandas as pd
from script import clean_dataframe

def test_clean_dataframe():
    df = pd.DataFrame({
        " name ": [" a ", " b ", None],
        "value": [1, None, 3]
    })
    result = clean_dataframe(df)
    
    # Pastikan kolom sudah bersih
    assert "name" in result.columns
    # Pastikan whitespace hilang
    assert result.loc[0, "name"] == "a"
    # Pastikan NaN numerik jadi 0
    assert result.loc[1, "value"] == 0
    # Pastikan row kosong di-drop
    assert result.shape[0] == 3
