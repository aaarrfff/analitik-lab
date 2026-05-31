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
# --- TAB 4: IDENTIFIKASI ION (SKEMA CAMPURAN GOL. I-V) ---
with tab4:
    st.header("Pemisahan Kation Golongan I-V")
    st.write("Berdasarkan Skema: $Ag^+$, $Pb^{2+}$, $Hg_2^{2+}$, $Al^{3+}$, $Fe^{3+}$, $Ba^{2+}$, $Sr^{2+}$, $Ca^{2+}$")

    st.subheader("Tahap 1: Penambahan HCl encer")
    tahap_1 = st.radio(
        "Pilih jalur berdasarkan hasil reaksi dengan HCl encer:",
        ["Terbentuk Endapan (AgCl, PbCl2, Hg2Cl2)", "Berupa Filtrat (Al3+, Fe3+, Ba2+, Sr2+, Ca2+)"],
        index=None
    )

    st.divider()

    # ================= LOGIKA GOLONGAN I =================
    if tahap_1 == "Terbentuk Endapan (AgCl, PbCl2, Hg2Cl2)":
        st.info("🧪 Fokus pada Endapan: Tambahkan $H_2O$ (cuci) lalu panaskan dengan $H_2O$.")
        tahap_2_gol1 = st.radio("Apa yang terjadi pada endapan setelah dipanaskan?", 
            ["Endapan Larut (Pb2+)", "Endapan Tidak Larut (AgCl, Hg2Cl2)"], index=None)
        
        if tahap_2_gol1 == "Endapan Larut (Pb2+)":
            st.write("➡️ Tambahkan $K_2CrO_4$")
            st.success("✨ Terbentuk endapan $PbCrO_4$ kuning. Kation: **Timbal ($Pb^{2+}$)**")
            
        elif tahap_2_gol1 == "Endapan Tidak Larut (AgCl, Hg2Cl2)":
            st.write("➡️ Tambahkan $NH_4OH$ berlebih (>>)")
            tahap_3_gol1 = st.radio("Apa hasil penambahan amonia?", 
                ["Endapan Putih Hg(NH2)Cl + Hitam Hg", "Menjadi Larutan (Ag(NH3)2+ Cl-)"], index=None)
            
            if tahap_3_gol1 == "Endapan Putih Hg(NH2)Cl + Hitam Hg":
                st.success("✨ Kation: **Merkurium(I) ($Hg_2^{2+}$)**")
            elif tahap_3_gol1 == "Menjadi Larutan (Ag(NH3)2+ Cl-)":
                st.write("➡️ Tambahkan $HNO_3$")
                st.success("✨ Terbentuk endapan $AgCl$ putih. Kation: **Perak ($Ag^+$)**")

    # ================= LOGIKA GOLONGAN III & IV =================
    elif tahap_1 == "Berupa Filtrat (Al3+, Fe3+, Ba2+, Sr2+, Ca2+)":
        st.info("🧪 Fokus pada Filtrat: Tambahkan $NH_4OH$ berlebih (>>).")
        tahap_2_filtrat = st.radio("Apa yang terbentuk?", 
            ["Terbentuk Endapan (Al(OH)3, Fe(OH)3)", "Berupa Filtrat (Ba2+, Sr2+, Ca2+)"], index=None)
        
        if tahap_2_filtrat == "Terbentuk Endapan (Al(OH)3, Fe(OH)3)":
            st.write("➡️ Tambahkan $NaOH$")
            tahap_3_gol3 = st.radio("Apa hasil penambahan NaOH?", 
                ["Endapan Fe(OH)3 (Tidak larut)", "Larutan Al(OH)4- (Larut)"], index=None)
            
            if tahap_3_gol3 == "Endapan Fe(OH)3 (Tidak larut)":
                st.write("➡️ Tambahkan $HNO_3$ (menjadi $Fe^{3+}$), lalu tambahkan $SCN^-$")
                st.success("✨ Terbentuk kompleks $Fe(SCN)_3$ merah. Kation: **Besi(III) ($Fe^{3+}$)**")
            elif tahap_3_gol3 == "Larutan Al(OH)4- (Larut)":
                st.write("➡️ Tambahkan $HCl$ lalu $Na_2CO_3$")
                st.success("✨ Terbentuk endapan $Al(OH)_3$ putih. Kation: **Aluminium ($Al^{3+}$)**")
                
        elif tahap_2_filtrat == "Berupa Filtrat (Ba2+, Sr2+, Ca2+)":
            st.write("➡️ Tambahkan $K_2CrO_4$")
            tahap_3_gol4 = st.radio("Apa hasilnya?", 
                ["Terbentuk Endapan (BaCrO4, SrCrO4)", "Berupa Filtrat (Ca2+)"], index=None)
            
            if tahap_3_gol4 == "Terbentuk Endapan (BaCrO4, SrCrO4)":
                st.write("➡️ Tambahkan $CH_3COOH$")
                tahap_4_gol4 = st.radio("Hasil penambahan asam asetat:", 
                    ["Endapan BaCrO4 Kuning", "Larutan Sr2+"], index=None)
                
                if tahap_4_gol4 == "Endapan BaCrO4 Kuning":
                    st.success("✨ Kation: **Barium ($Ba^{2+}$)**")
                elif tahap_4_gol4 == "Larutan Sr2+":
                    st.write("➡️ Tambahkan $Na_2CO_3$")
                    st.success("✨ Terbentuk endapan $SrCO_3$ putih. Kation: **Stronsium ($Sr^{2+}$)**")
                    
            elif tahap_3_gol4 == "Berupa Filtrat (Ca2+)":
                st.write("➡️ Tambahkan $H_2C_2O_4$ dan $NH_4OH$")
                st.success("✨ Terbentuk endapan $CaC_2O_4$ putih. Kation: **Kalsium ($Ca^{2+}$)**")
            st.success("✨ Logam Teridentifikasi: **Kalium ($K^+$)**")
