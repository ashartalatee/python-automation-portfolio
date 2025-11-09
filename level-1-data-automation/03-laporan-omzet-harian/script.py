import pandas as pd

def load_data(file_path):
    """
    Load file Excel penjualan.
    """
    df = pd.read_excel(file_path)
    return df

def calculate_daily_omzet(df):
    """
    Hitung omzet per tanggal.
    """
    df['Total'] = df['Qty'] * df['Harga']
    omzet = df.groupby('Tanggal')['Total'].sum().reset_index()
    return omzet

def top_selling_products(df, top_n=5):
    """
    Ambil produk terlaris.
    """
    product_sales = df.groupby('Produk')['Qty'].sum().reset_index()
    top_products = product_sales.sort_values(by='Qty', ascending=False).head(top_n)
    return top_products
