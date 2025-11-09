import pandas as pd
import os

# -----------------------
# Generate Laporan
# -----------------------
def generate_report(df):
    total_omzet = df['Harga'] * df['Qty']
    df['Total'] = total_omzet

    summary = df.groupby('Produk')['Total'].sum().sort_values(ascending=False).reset_index()

    report_file = "laporan_harian.xlsx"
    with pd.ExcelWriter(report_file) as writer:
        df.to_excel(writer, index=False, sheet_name="Detail")
        summary.to_excel(writer, index=False, sheet_name="Ringkasan")
    
    return report_file


# -----------------------
# Kirim Laporan WA atau Email
# -----------------------
def send_report(file_path, recipient):
    try:
        if recipient.startswith("+"):  # Kirim WA
            import pywhatkit as kit
            import time
            print("Membuka WA Web untuk kirim gambar...")
            kit.sendwhats_image(recipient, file_path, "Laporan hari ini", 15, True, 5)
            print("WA terkirim!")
            return True
        else:  # Kirim Email
            import smtplib
            from email.message import EmailMessage

            # Ganti dengan email kamu
            EMAIL_ADDRESS = "your_email@gmail.com"
            EMAIL_PASSWORD = "your_app_password"

            msg = EmailMessage()
            msg['Subject'] = "Laporan Harian"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = recipient
            msg.set_content("Berikut laporan harian Anda.")

            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Email terkirim!")
            return True

    except Exception as e:
        print("Error kirim laporan:", e)
        return False
