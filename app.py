import streamlit as st
import requests

# Konfigurasi data yang kamu berikan
FIGMA_TOKEN = "Figd_HZpZQ5y4W8U6dV13kaFZHjLJ4ob-Pl84V4enr7ZR"
FILE_KEY = "RdHFVDAXuQqS3CDFVAhKTC"

def get_figma_data():
    url = f"https://api.figma.com/v1/files/{FILE_KEY}"
    headers = {"X-Figma-Token": FIGMA_TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()

st.set_page_config(page_title="J-Mailbox Dashboard", layout="wide")

st.title("🚀 J-Mailbox AI Dashboard")
st.write("Menghubungkan desain Figma ke Streamlit...")

if st.sidebar.button("Sinkronisasi dengan Figma"):
    data = get_figma_data()
    
    if 'name' in data:
        st.sidebar.success(f"Terkoneksi ke: {data['name']}")
        
        # Contoh mengambil Nama File dan Versi
        st.subheader("Informasi Proyek")
        col1, col2 = st.columns(2)
        col1.metric("Nama Desain", data['name'])
        col2.metric("Terakhir Diupdate", data['lastModified'][:10])
        
        # Menampilkan Struktur Layer (Opsional - untuk debugging)
        with st.expander("Lihat Struktur Data JSON"):
            st.json(data)
    else:
        st.sidebar.error("Gagal mengambil data. Cek Token/Key.")

# Simulasi Tampilan Dashboard (Bisa kamu sesuaikan dengan isi Figma kamu)
st.divider()
c1, c2, c3 = st.columns(3)
c1.info("📬 Total Mails: 1,234")
c2.success("🤖 AI processed: 890")
c3.warning("⚠️ Spam detected: 12")