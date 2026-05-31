import streamlit as st
# Pengaturan halaman utama
st.set_page_config(
    page_title="Asisten Lab Kimia Analitik",
    page_icon="🧪",
    layout="wide"
)

# Judul Aplikasi
st.title("🧪 Asisten Digital Laboratorium Analitik")
st.write("Yuk cari tahu senyawa apa yang ingin kamu ketahui")

# Membuat Menu menggunakan Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Gugus Fungsi", 
    "🧮 Yield", 
    "📚 Reagen",
    "⚡ Identifikasi Ion (Analitik)"
])
# --- TAB 4: IDENTIFIKASI ION LOGAM & NON-LOGAM ---
with tab4:
    st.header("Sistem Identifikasi Kation & Anion (Kualitatif)")
    st.write("Berdasarkan penambahan reagen spesifik dan uji nyala api.")

    kategori_uji = st.radio("Pilih Kategori Analisis:", ["Uji Kation (Logam)", "Uji Anion (Non-Logam)", "Uji Nyala Api (Flame Test)"])

    st.divider()

    if kategori_uji == "Uji Kation (Logam)":
        st.subheader("Uji Kation Golongan I (Penambahan HCl encer)")
        hasil_hcl = st.radio("Apa yang terjadi saat sampel ditambah HCl encer?", [
            "Terbentuk endapan putih",
            "Tidak ada endapan / larutan jernih"
        ])

        if hasil_hcl == "Terbentuk endapan putih":
            st.info("Kemungkinan Kation Golongan I: $Ag^+$, $Pb^{2+}$, atau $Hg_2^{2+}$")
            
            hasil_panas = st.radio("Apa yang terjadi saat endapan dipanaskan dengan air?", [
                "Endapan larut",
                "Endapan tidak larut"
            ])
            
            if hasil_panas == "Endapan larut":
                st.success("✨ Kation Teridentifikasi: **Timbal ($Pb^{2+}$)**")
            elif hasil_panas == "Endapan tidak larut":
                hasil_nh3 = st.radio("Apa yang terjadi saat ditambah amonia ($NH_3$) encer?", [
                    "Endapan larut kembali",
                    "Endapan berubah menjadi hitam/abu-abu"
                ])
                if hasil_nh3 == "Endapan larut kembali":
                    st.success("✨ Kation Teridentifikasi: **Perak ($Ag^+$)**")
                elif hasil_nh3 == "Endapan berubah menjadi hitam/abu-abu":
                    st.success("✨ Kation Teridentifikasi: **Merkurium(I) ($Hg_2^{2+}$)**")
        else:
            st.warning("Bukan Kation Golongan I. Lanjutkan ke pengujian Golongan II dengan mengalirkan gas $H_2S$.")

    elif kategori_uji == "Uji Anion (Non-Logam)":
        st.subheader("Uji Identifikasi Anion Spesifik")
        reagen_anion = st.selectbox("Pilih reagen yang ditambahkan ke sampel:", [
            "BaCl2 (Barium Klorida)",
            "AgNO3 (Perak Nitrat)",
            "FeSO4 + H2SO4 pekat (Uji Cincin Cokelat)"
        ])

        if reagen_anion == "BaCl2 (Barium Klorida)":
            st.write("Hasil: Terbentuk endapan putih yang **tidak larut** dalam HCl encer.")
            st.success("✨ Anion Teridentifikasi: **Sulfat ($SO_4^{2-}$)**")
        
        elif reagen_anion == "AgNO3 (Perak Nitrat)":
            hasil_agno3 = st.radio("Warna endapan yang terbentuk:", ["Putih", "Kuning Pucat", "Kuning Terang"])
            if hasil_agno3 == "Putih":
                st.success("✨ Anion Teridentifikasi: **Klorida ($Cl^-$)**")
            elif hasil_agno3 == "Kuning Pucat":
                st.success("✨ Anion Teridentifikasi: **Bromida ($Br^-$)**")
            elif hasil_agno3 == "Kuning Terang":
                st.success("✨ Anion Teridentifikasi: **Iodida ($I^-$)**")
                
        elif reagen_anion == "FeSO4 + H2SO4 pekat (Uji Cincin Cokelat)":
            st.write("Hasil: Terbentuk cincin berwarna cokelat di antara dua lapisan cairan.")
            st.success("✨ Anion Teridentifikasi: **Nitrat ($NO_3^-$)**")

    elif kategori_uji == "Uji Nyala Api (Flame Test)":
        st.subheader("Uji Nyala Logam Alkali & Alkali Tanah")
        warna_nyala = st.selectbox("Pilih warna nyala api yang terlihat:", [
            "Kuning keemasan intens",
            "Merah bata / Merah jingga",
            "Hijau kekuningan / Hijau apel",
            "Merah tua (Crimson)",
            "Ungu / Lilac"
        ])

        if warna_nyala == "Kuning keemasan intens":
            st.success("✨ Logam Teridentifikasi: **Natrium ($Na^+$)**")
        elif warna_nyala == "Merah bata / Merah jingga":
            st.success("✨ Logam Teridentifikasi: **Kalsium ($Ca^{2+}$)**")
        elif warna_nyala == "Hijau kekuningan / Hijau apel":
            st.success("✨ Logam Teridentifikasi: **Barium ($Ba^{2+}$)**")
        elif warna_nyala == "Merah tua (Crimson)":
            st.success("✨ Logam Teridentifikasi: **Stronsium ($Sr^{2+}$)** atau **Litium ($Li^+$)**")
        elif warna_nyala == "Ungu / Lilac":
            st.success("✨ Logam Teridentifikasi: **Kalium ($K^+$)**")
