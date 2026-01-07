import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np  # PERLU DITAMBAHKAN
import base64
import os

# ============================
#   KONFIGURASI HALAMAN
# ============================
st.set_page_config(page_title="Kalkulator PLTS & Edukasi", layout="wide")

# ============================
#   FUNGSI BACKGROUND IMAGE & STYLE
# ============================
def set_background(image_file):
    if not os.path.exists(image_file):
        return
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    
    st.markdown(
        f"""
        <style>
        /* 1. Background Utama Aplikasi (Tetap sama) */
        .stApp {{
            background-image: url("data:image/png;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* 2. Sidebar: Ubah Putih jadi Hitam Transparan */
        section[data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0, 0.75) !important; /* Hitam transparan */
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255,255,255,0.1); /* Garis pinggir samar */
        }}
        
        /* Paksa semua teks di sidebar jadi Putih */
        section[data-testid="stSidebar"] * {{
            color: white !important;
            text-shadow: none !important;
        }}

        /* 3. Input Fields (Kotak Isian): Ubah Background Putih jadi Abu Gelap */
        section[data-testid="stSidebar"] div[data-baseweb="input"],
        section[data-testid="stSidebar"] div[data-baseweb="base-input"],
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
            background-color: #262730 !important; /* Abu gelap */
            border: 1px solid #4c4c4c !important; /* Border abu */
            color: white !important; 
        }}
        
        /* Teks di dalam input */
        section[data-testid="stSidebar"] div[data-baseweb="input"] > div {{
            background-color: transparent !important;
            color: white !important;
        }}

        /* 4. Tulisan Bold/Kuat */
        section[data-testid="stSidebar"] .stMarkdown > div > strong {{
            color: #f0f0f0 !important; /* Putih terang */
        }}

        /* 5. Tombol (Buttons) */
        section[data-testid="stSidebar"] button {{
             background-color: #262730 !important;
             color: white !important;
             border-color: #4c4c4c !important;
        }}

        /* 6. Ikon (SVG) */
        section[data-testid="stSidebar"] svg {{
            fill: white !important;
            stroke: white !important;
        }}

        /* 7. Dropdown Menu (Pilihan yang muncul saat diklik) */
        div[data-baseweb="popover"],
        div[data-baseweb="popover"] > div,
        ul[data-baseweb="menu"] {{
            background-color: #262730 !important;
            border: 1px solid #4c4c4c !important;
        }}

        /* Pilihan di dalam dropdown */
        li[role="option"] {{
            color: white !important;
            background-color: #262730 !important;
        }}

        /* Saat mouse diarahkan ke pilihan (Hover) */
        li[role="option"]:hover, li[role="option"][aria-selected="true"] {{
            background-color: #ff4b4b !important; /* Merah Streamlit atau warna lain */
            color: white !important;
        }}

        /* Header transparan */
        header {{ background: transparent !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )
# --- LOAD GAMBAR ---
nama_file_gambar = "energi_terbarukan.jpg" 

if os.path.exists(nama_file_gambar):
    set_background(nama_file_gambar)
else:
    st.markdown("""<style>.stApp { background-color: #f0f2f6; }</style>""", unsafe_allow_html=True)

# ============================
#   STYLE CSS KONTEN
# ============================
st.markdown("""
    <style>
    .card {
        background-color: rgba(255, 255, 255, 0.95) !important;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 1);
    }
    .card * { color: #333333 !important; font-family: 'Segoe UI', sans-serif; }
    .card h2 { color: #0652DD !important; font-weight: 800 !important; font-size: 2.2rem !important; margin-bottom: 5px !important; }
    .card h3 { color: #666666 !important; font-size: 1rem !important; text-transform: uppercase; letter-spacing: 1px; }
    
    .title-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .main-title { color: #0652DD !important; font-weight: 900; font-size: 2.8rem; margin: 0; }
    .sub-title { color: #333333 !important; font-weight: bold; font-size: 1.2rem; margin-top: 5px; }

    table { width: 100%; border-collapse: separate; border-spacing: 0; background-color: #ffffff !important; color: #000000 !important; border-radius: 10px; overflow: hidden; margin-top: 0px; }
    th { background-color: #0652DD !important; color: white !important; padding: 15px; text-align: left; }
    td { padding: 15px; border-bottom: 1px solid #eee; color: #000000 !important; font-weight: 500; }

    .info-container { background-color: #ffffff !important; border-radius: 12px; padding: 20px; margin-top: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: left; }
    .bat-border { border-left: 6px solid #0652DD; }
    .scc-border { border-left: 6px solid #2ecc71; }
    .info-container h3 { margin-top: 0; font-weight: bold; font-size: 1.1rem; }
    .bat-border h3 { color: #0652DD !important; }
    .scc-border h3 { color: #2ecc71 !important; }
    .info-container p { color: #333333 !important; line-height: 1.5; margin-bottom: 5px; }
    
    .warning-box { background-color: #fffde7 !important; border-left: 6px solid #fbc02d; padding: 15px; margin-bottom: 20px; border-radius: 8px; color: #333333 !important; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)


# ============================
#   SIDEBAR INPUT
# ============================
st.sidebar.markdown("### ⚙️ Konfigurasi Sistem")

tipe_sistem = st.sidebar.selectbox("Tipe Sistem PLTS", 
    ["DC Only (Tanpa Inverter)", "Off-Grid (Baterai Mandiri)", "Hybrid (Grid + Baterai)", "On-Grid (Hemat Tagihan PLN)"])

st.sidebar.markdown("---")

tab_beban, tab_pv, tab_bat_inv = st.sidebar.tabs(["⚡ Beban", "🔆 Panel", "🔋 Komponen"])

# --- TAB BEBAN & ENERGI ---
with tab_beban:
    metode_input = st.radio("Metode Perhitungan Beban", ["Berdasarkan Tagihan (Rp)", "Berdasarkan Daya Alat (Watt)"])
    kwh_harian = 0; tarif_pln_per_kwh = 1445; tagihan = 0 

    if "Tagihan" in metode_input:
        if "DC Only" in tipe_sistem:
            st.info("ℹ️ Mode DC: Masukkan estimasi biaya listrik setara.")
            tarif_pln_per_kwh = 1445 
        else:
            golongan_tarif = {
                "R-1/900 VA (RTM)": 1352, "R-1/1300 VA": 1445, "R-1/2200 VA": 1445,
                "R-2/3500-5500 VA": 1700, "R-3/6600 VA ke atas": 1700,
                "Bisnis/Industri (>200kVA)": 1115, "Manual Input": 0
            }
            pilihan_golongan = st.selectbox("Golongan Tarif PLN", list(golongan_tarif.keys()), index=1)
            if pilihan_golongan == "Manual Input":
                tarif_pln_per_kwh = st.number_input("Harga Listrik per kWh (Rp)", value=1445)
            else:
                tarif_pln_per_kwh = golongan_tarif[pilihan_golongan]

        tagihan = st.number_input("💵 Tagihan/Kebutuhan (Rp)", min_value=50000, value=100000, step=10000)
        kwh_harian = (tagihan / tarif_pln_per_kwh / 30) * 1000
    else:
        st.info("Masukkan total daya alat yang ingin dinyalakan.")
        beban_watt = st.number_input("Total Daya Alat (Watt)", min_value=1, value=24, step=1)
        durasi_jam = st.number_input("Lama Nyala per Hari (Jam)", min_value=1, max_value=24, value=12, step=1)
        wh_harian = beban_watt * durasi_jam
        kwh_harian = wh_harian 
        tagihan = (kwh_harian / 1000) * 30 * tarif_pln_per_kwh
        
    st.markdown(f"**💡 Kebutuhan Energi Harian (Wh):** `{kwh_harian:,.0f} Wh`")
    st.markdown(f"**Tarif PLN/kWh:** `Rp {tarif_pln_per_kwh:,.0f}`")

    persen_ekspor = 0; harga_ekspor = 0
    if "On-Grid" in tipe_sistem:
        st.markdown("---")
        st.markdown("### 🔌 Skema Ekspor")
        skema_aturan = st.radio("Aturan Ekspor Listrik", ["Permen No 2 Tahun 2024 (Baru)", "Permen Lama"])
        harga_ekspor = 0 if "Baru" in skema_aturan else tarif_pln_per_kwh * 0.65
        persen_ekspor = st.slider("Daya Diekspor (%)", 0, 100, 30)

# --- TAB PANEL SURYA ---
with tab_pv:
    st.markdown("### 🔆 Spesifikasi Panel")
    jenis_panel = st.selectbox("Jenis Panel", ["Monocrystalline", "Polycrystalline", "Thin Film"])
    panel_wp = st.selectbox("Ukuran Panel (Wp)", [30, 50, 100, 200, 300, 400, 450, 500, 550], index=4)
    st.markdown("---")
    biaya_instalasi_rp = st.number_input("🏗 Biaya Instalasi (Rp)", value=1000000)

# --- TAB KOMPONEN LAIN ---
biaya_inverter = 0; kapasitas_inverter = 0; tipe_inverter = "-"; biaya_aksesoris_dc = 0; jenis_aksesoris_dc = "-"
biaya_scc = 0; jenis_scc = "Tidak Perlu (On-Grid)"; biaya_baterai_total = 0; jumlah_sel_total = 0; konfigurasi_baterai = "-"; nama_bms = "-"; biaya_bms = 0
target_volt_sistem = 0

with tab_bat_inv:
    if "DC Only" in tipe_sistem:
        st.markdown("### 🔌 Distribusi DC")
        jenis_aksesoris_dc = st.text_input("Nama Komponen DC", value="Box Sekring & Step Down")
        biaya_aksesoris_dc = st.number_input("Biaya Aksesoris DC (Rp)", value=500000, step=50000)
    else:
        st.markdown("### 🔌 Inverter & SCC")
        if "Off-Grid" in tipe_sistem:
            list_inverter = ["Off-Grid Inverter (Pure Sine Wave)", "Hybrid Inverter (All-in-One)"]
        elif "Hybrid" in tipe_sistem:
            list_inverter = ["Hybrid Inverter (All-in-One)", "Off-Grid Inverter + Charger"]
        else:
            list_inverter = ["On-Grid Inverter (Grid Tie)"]
        tipe_inverter = st.selectbox("Jenis Inverter", list_inverter)
        kapasitas_inverter = st.number_input("Kapasitas Inverter (Watt)", min_value=450, value=2000, step=500)
        harga_inv_per_watt = 2000 if "Hybrid" in tipe_sistem else (1500 if "On-Grid" in tipe_sistem else 1800)
        biaya_inverter = kapasitas_inverter * harga_inv_per_watt
        
        if "On-Grid" not in tipe_sistem:
            if "DC Only" not in tipe_sistem:
                st.markdown("---")
            jenis_scc = st.radio("Teknologi SCC", ["MPPT (Efisien)", "PWM (Murah)"])

    if "On-Grid" not in tipe_sistem:
        st.markdown("---")
        st.markdown("### 🔋 Rakitan Baterai")
        
        opsi_volt = [12, 24] if "DC Only" in tipe_sistem else [12, 24, 48]
        target_volt_sistem = st.selectbox("Target Voltase Sistem (V)", opsi_volt, index=0)
        jenis_kimia = st.selectbox("Jenis Baterai", ["Lithium Iron Phosphate (LiFePO4)", "Lithium Ion (Li-ion)", "Lead Acid / Aki"])
        
        if "LiFePO4" in jenis_kimia:
            opsi_tegangan = [3.2, 12.8]
            format_label = {3.2: "3.2V (Cell Satuan)", 12.8: "12.8V (Battery Pack 4S)"}
        elif "Li-ion" in jenis_kimia:
            opsi_tegangan = [3.7]
            format_label = {3.7: "3.7V (Cell Satuan)"}
        else:
            opsi_tegangan = [12.0]
            format_label = {12.0: "12V (Aki Basah/Kering)"}

        volt_per_sel = st.selectbox("Tegangan Sel (V)", options=opsi_tegangan, format_func=lambda x: format_label[x])

        def_ah = 0; def_rp = 0
        if volt_per_sel == 3.2: def_ah = 100; def_rp = 450000
        elif volt_per_sel == 12.8: def_ah = 100; def_rp = 3500000
        elif volt_per_sel == 3.7: def_ah = 20; def_rp = 35000
        else: def_ah = 100; def_rp = 2000000
                
        ah_per_sel = st.number_input("Kapasitas Sel (Ah)", value=def_ah, min_value=1)
        harga_bat_satuan = st.number_input("Harga Sel (Rp)", value=def_rp, step=10000)

        est_seri = math.ceil(target_volt_sistem / volt_per_sel)
        
        if est_seri > 1 and ("Lithium" in jenis_kimia):
            st.markdown("#### 🛡️ Modul BMS (Battery Management)")
            
            if "LiFePO4" in jenis_kimia:
                rec_name = f"BMS {est_seri}S LiFePO4 12V/24V 30A"
                rec_price = 45000 
                if est_seri >= 8: rec_price = 52000 
                
            elif "Li-ion" in jenis_kimia:
                rec_name = f"BMS {est_seri}S Li-ion 12V/24V 15A"
                rec_price = 52000
                if est_seri <= 4: rec_price = 45000

            else:
                rec_name = f"BMS {est_seri}S Universal"
                rec_price = 50000

            st.info(f"Sistem {target_volt_sistem}V terdeteksi butuh BMS {est_seri}S.")
            nama_bms = st.text_input("Tipe BMS", value=rec_name)
            biaya_bms = st.number_input("Harga BMS (Rp)", value=rec_price, step=500)
        else:
            biaya_bms = 0
            nama_bms = "-"

# ============================
#   LOGIKA PERHITUNGAN UTAMA
# ============================
if "DC Only" in tipe_sistem: eff = 0.95 
elif "On-Grid" in tipe_sistem: eff = 0.9
else: eff = 0.8

total_wp_needed = (kwh_harian / eff) / 3.5 
jumlah_panel = math.ceil(total_wp_needed / panel_wp)
total_wp_aktual = jumlah_panel * panel_wp
harga_per_wp = 5200 if jenis_panel == "Monocrystalline" else 4500
biaya_panel_total = total_wp_aktual * harga_per_wp

desc_baterai_singkat = "Tanpa Baterai"; volt_sistem_final = 0; kwh_total = 0
if "On-Grid" not in tipe_sistem:
    volt_sistem_final = target_volt_sistem 
    kebutuhan_wh_real = kwh_harian * (0.6 if "Hybrid" not in tipe_sistem else 0.4)
    dod = 0.8 if "Lithium" in jenis_kimia else 0.5
    
    target_ah_sistem = (kebutuhan_wh_real / dod) / target_volt_sistem
    jumlah_seri = math.ceil(target_volt_sistem / volt_per_sel)
    jumlah_paralel = math.ceil(target_ah_sistem / ah_per_sel)
    
    jumlah_sel_total = jumlah_seri * jumlah_paralel
    biaya_baterai_total = jumlah_sel_total * harga_bat_satuan
    
    volt_aktual = jumlah_seri * volt_per_sel
    ah_aktual = jumlah_paralel * ah_per_sel
    kwh_total = (volt_aktual * ah_aktual) / 1000
    
    konfigurasi_baterai = f"<b>{jumlah_seri} Seri</b> x <b>{jumlah_paralel} Paralel</b><br>Total: {jumlah_sel_total} Sel ({volt_aktual:.1f}V {ah_aktual}Ah)"
    desc_baterai_singkat = f"{jumlah_sel_total}x {jenis_kimia.split(' ')[0]} ({jumlah_seri}S{jumlah_paralel}P)"

raw_ampere = 0
if "On-Grid" not in tipe_sistem:
    raw_ampere = total_wp_aktual / target_volt_sistem
    scc_ampere_needed = math.ceil(raw_ampere * 1.25 / 10) * 10 
    if scc_ampere_needed < 10: scc_ampere_needed = 10
    scc_desc = f"{jenis_scc.split(' ')[0]} {scc_ampere_needed}A"
    
    if "All-in-One" in tipe_inverter:
        biaya_scc = 0; scc_status = "Integrated (Built-in Inverter)"
    else:
        scc_status = "Terpisah"
        if "MPPT" in jenis_scc: biaya_scc = scc_ampere_needed * 35000 
        else: biaya_scc = scc_ampere_needed * 4000; 
        if biaya_scc < 100000: biaya_scc = 100000

total_investasi = biaya_panel_total + biaya_baterai_total + biaya_inverter + biaya_scc + biaya_instalasi_rp + biaya_aksesoris_dc + biaya_bms

produksi_kwh_bulan = (total_wp_aktual * 3.5 * 30) / 1000 
if "Off-Grid" in tipe_sistem or "DC Only" in tipe_sistem:
    penghematan_bulanan = tagihan
else: 
    kwh_sendiri = produksi_kwh_bulan * ((100 - persen_ekspor) / 100)
    kwh_ekspor = produksi_kwh_bulan * (persen_ekspor / 100)
    penghematan_bulanan = (kwh_sendiri * tarif_pln_per_kwh) + (kwh_ekspor * harga_ekspor)
    if penghematan_bulanan > tagihan: penghematan_bulanan = tagihan
    
delta_hemat = penghematan_bulanan / tagihan * 100 if tagihan > 0 else 0
sisa_tagihan = max(0, tagihan - penghematan_bulanan)
roi_tahun = total_investasi / (penghematan_bulanan * 12) if penghematan_bulanan > 0 else 99

# ============================
#   MENU TABS UTAMA (DASHBOARD vs EDUKASI)
# ============================
tab_kalkulator, tab_edukasi = st.tabs(["📊 Kalkulator Sistem", "🎓 Edukasi Sensor"])

# ============================
#   TAB 1: KALKULATOR UTAMA
# ============================
with tab_kalkulator:
    st.markdown(f"""
    <div class="title-container">
        <div class='main-title'>🔆 Kalkulator PLTS</div>
        <div class='sub-title'>Simulasi Sistem: **{tipe_sistem}** | Kapasitas: **{(total_wp_aktual/1000):.1f} kWp**</div>
    </div>
    """, unsafe_allow_html=True)

    if "On-Grid" in tipe_sistem and harga_ekspor == 0 and persen_ekspor > 0:
        st.markdown("<div class='warning-box'>⚠️ **Peringatan:** Aturan Permen ESDM No 2/2024 menetapkan ekspor listrik ke PLN bernilai **Rp 0** (tanpa kompensasi).</div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1: 
        st.metric(label="💰 Total Investasi", value=f"Rp {total_investasi/1000000:.1f} Juta", delta=f"Rp {biaya_panel_total/1000000:.1f} Jt (Panel)")
    with col2: 
        st.metric(label="📉 Penghematan Bulanan", value=f"Rp {penghematan_bulanan:,.0f}", delta=f"{delta_hemat:.1f}% dari Tagihan", delta_color="inverse")
    with col3: 
        st.metric(label="⏳ Estimasi Balik Modal (ROI)", value=f"{roi_tahun:.1f} Tahun", delta=f"Rp {sisa_tagihan:,.0f} Sisa Tagihan")
    with col4: 
        st.metric(label="⚡ Output Energi Bulanan", value=f"{produksi_kwh_bulan:,.0f} kWh", delta=f"{jumlah_panel} Panel {panel_wp}Wp")
        
    st.markdown("---")

    col_r1, col_g1, col_g2 = st.columns([1.5, 1, 1])

    with col_r1:
        st.markdown("### 🧩 Rincian Teknis Sistem")
        
        if "On-Grid" not in tipe_sistem:
            st.markdown(f"""
            <div class='info-container bat-border'>
                <h3>🔋 Detail Rakitan Baterai ({target_volt_sistem}V)</h3>
                <p><b>Konfigurasi:</b> {konfigurasi_baterai}</p>
                <p><b>Kapasitas Total:</b> {kwh_total:.2f} kWh (Neto)</p>
                <p><i>{desc_baterai_singkat} | Est. Biaya: Rp {biaya_baterai_total:,.0f}</i></p>
                {'<p><b>BMS:</b> ' + nama_bms + ' (Est: Rp ' + f'{biaya_bms:,.0f})</p>' if biaya_bms > 0 else ''}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='info-container scc-border'>
                <h3>🔌 Rekomendasi SCC (Controller)</h3>
                <p><b>Panel:</b> {total_wp_aktual} Wp (Max Arus ±{raw_ampere:.1f} A)</p>
                <p><b>Disarankan:</b> SCC **{scc_desc}** (Min **{scc_ampere_needed}A**)</p>
                <p><i>Status SCC: **{scc_status}** (Est: Rp {biaya_scc:,.0f})</i></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(f"Sistem **{tipe_sistem}** tidak memerlukan Baterai dan SCC terpisah.")
            st.markdown(f"""
            <div class='info-container bat-border'>
                <h3>🔌 Inverter Grid-Tie</h3>
                <p><b>Tipe:</b> {tipe_inverter} ({kapasitas_inverter}W)</p>
                <p><b>Est. Biaya:</b> Rp {biaya_inverter:,.0f}</p>
                <p><i>Perkiraan harga {harga_inv_per_watt} Rp/Watt.</i></p>
            </div>
            """, unsafe_allow_html=True)

    with col_g1:
        st.markdown("<div class='card'><h3>📊 Potensi Penghematan</h3>", unsafe_allow_html=True)
        fig1, ax1 = plt.subplots(figsize=(5, 3), dpi=150)
        sisa = max(0, tagihan - penghematan_bulanan)
        bars = ax1.bar(['Tagihan Awal', 'Sisa'], [tagihan, sisa], color=['#ff6b6b', '#1dd1a1'])
        ax1.bar_label(bars, fmt='Rp %.0f', padding=3)
        ax1.spines['top'].set_visible(False); ax1.spines['right'].set_visible(False); ax1.spines['left'].set_visible(False); ax1.get_yaxis().set_ticks([])
        fig1.patch.set_alpha(1.0); ax1.patch.set_alpha(1.0)
        st.pyplot(fig1)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_g2:
        st.markdown("<div class='card'><h3>📊 Komposisi Biaya</h3>", unsafe_allow_html=True)
        clean_v = [v for v in [biaya_panel_total, biaya_baterai_total, biaya_inverter, biaya_scc, biaya_instalasi_rp, biaya_aksesoris_dc, biaya_bms] if v > 0]
        clean_l = [l for l,v in zip(["Panel", "Baterai", "Inverter", "SCC", "Instalasi", "Aksesoris DC", "BMS"], [biaya_panel_total, biaya_baterai_total, biaya_inverter, biaya_scc, biaya_instalasi_rp, biaya_aksesoris_dc, biaya_bms]) if v > 0]
        
        if len(clean_v) == 0:
            st.info("Komposisi biaya belum tersedia.")
        else:
            fig2, ax2 = plt.subplots(figsize=(5, 3), dpi=150)
            wedges, texts, autotexts = ax2.pie(clean_v, labels=clean_l, autopct='%1.1f%%', colors=['#54a0ff', '#feca57', '#5f27cd', '#badc58', '#c8d6e5', '#ff9f43', '#ff6b6b'], textprops={'color': "#333333", 'fontsize': 10})
            for t in autotexts: t.set_weight('bold'); t.set_color('white'); t.set_fontsize(9)
            fig2.patch.set_alpha(1.0); ax2.patch.set_alpha(1.0)
            st.pyplot(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("🧾 Lihat Rincian Anggaran Biaya (RAB)"):
        rows_html = ""
        rows_html += f"<tr><td>Panel Surya</td><td>{jenis_panel} ({panel_wp}Wp)</td><td>{jumlah_panel}</td><td>Rp {harga_per_wp*panel_wp:,.0f}</td><td>Rp {biaya_panel_total:,.0f}</td></tr>"

        if "DC Only" in tipe_sistem:
            rows_html += f"<tr><td>Aksesoris DC</td><td>{jenis_aksesoris_dc}</td><td>1</td><td>Rp {biaya_aksesoris_dc:,.0f}</td><td>Rp {biaya_aksesoris_dc:,.0f}</td></tr>"
        else:
            rows_html += f"<tr><td>Inverter</td><td>{tipe_inverter} ({kapasitas_inverter}W)</td><td>1</td><td>Rp {biaya_inverter:,.0f}</td><td>Rp {biaya_inverter:,.0f}</td></tr>"

        if biaya_scc > 0 or ("All-in-One" in tipe_inverter):
            rows_html += f"<tr><td>SCC</td><td>{scc_desc} ({scc_status.split(' ')[0]})</td><td>1</td><td>Rp {biaya_scc:,.0f}</td><td>Rp {biaya_scc:,.0f}</td></tr>"
        
        if biaya_baterai_total > 0:
            rows_html += f"<tr><td>Baterai</td><td>{desc_baterai_singkat}</td><td>{jumlah_sel_total}</td><td>Rp {harga_bat_satuan:,.0f}</td><td>Rp {biaya_baterai_total:,.0f}</td></tr>"

        if biaya_bms > 0:
            rows_html += f"<tr><td>BMS</td><td>{nama_bms}</td><td>1</td><td>Rp {biaya_bms:,.0f}</td><td>Rp {biaya_bms:,.0f}</td></tr>"

        rows_html += f"<tr><td>Instalasi</td><td>Jasa & Kabel</td><td>1</td><td>Rp {biaya_instalasi_rp:,.0f}</td><td>Rp {biaya_instalasi_rp:,.0f}</td></tr>"

        total_row_html = f"""
        <tr style="background-color: #f4f4f4; border-top: 2px solid #cccccc;">
        <td colspan="4" style="text-align: right; font-weight: 800; color: #000000 !important; padding: 15px;">TOTAL INVESTASI</td>
        <td style="color: #0652DD !important; font-weight: 900; padding: 15px;">Rp {total_investasi:,.0f}</td>
        </tr>
        """

        table_html = f"""
        <div class="card" style="padding: 0; box-shadow: none; border: none;">
        <table>
        <thead><tr><th>Komponen</th><th>Spesifikasi</th><th>Qty</th><th>Harga Satuan</th><th>Total</th></tr></thead>
        <tbody>{rows_html}{total_row_html}</tbody>
        </table>
        </div>
        """
        st.markdown(table_html, unsafe_allow_html=True)

# ============================
#   TAB 2: EDUKASI SENSOR (FITUR BARU)
# ============================
with tab_edukasi:
    st.markdown("<div class='title-container'><div class='main-title'>🎓 Edukasi Sensor</div><div class='sub-title'>Simulasi Visual: Resolution, Accuracy, Fidelity, & Uncertainty</div></div>", unsafe_allow_html=True)
    
    st.markdown("""
    Gunakan **slider** di bawah untuk memanipulasi parameter sensor dan melihat bagaimana kualitas data berubah secara real-time.
    Ini mensimulasikan pembacaan Arus (Ampere) pada sistem PLTS saat cuaca berawan dinamis.
    """)

    # --- CONTROLS ---
    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1:
        res_val = st.slider("1. Resolution Step (A)", 0.1, 2.0, 1.0, step=0.1, help="Semakin besar nilai, semakin 'kotak-kotak' datanya.")
    with col_c2:
        bias_val = st.slider("2. Accuracy Bias (A)", -2.0, 2.0, 0.8, step=0.1, help="Pergeseran dari nilai nol (offset error).")
    with col_c3:
        lag_val = st.slider("3. Fidelity Lag", 0.01, 0.5, 0.05, help="Nilai kecil = Respon lambat (Lagging).")
    with col_c4:
        noise_val = st.slider("4. Uncertainty Noise", 0.1, 1.0, 0.3, help="Tingkat gangguan acak pada sinyal.")

    # --- SIMULATION LOGIC ---
    t = np.linspace(0, 100, 500)
    true_signal = 5 + 2 * np.sin(t / 10) 
    true_signal[200:300] = 2  # Drop tajam (awan)

    fig_sim, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    # 1. Resolution
    low_res_signal = np.round(true_signal / res_val) * res_val
    axs[0, 0].plot(t, true_signal, 'g', alpha=0.5, label='True')
    axs[0, 0].step(t, low_res_signal, 'r', where='mid', label=f'Res: {res_val}A')
    axs[0, 0].set_title('Resolution (Resolusi)')
    axs[0, 0].legend(loc='upper right', fontsize='small')
    axs[0, 0].grid(True, alpha=0.3)

    # 2. Accuracy
    inaccurate_signal = true_signal + bias_val
    axs[0, 1].plot(t, true_signal, 'g', alpha=0.5, label='True')
    axs[0, 1].plot(t, inaccurate_signal, 'r--', label=f'Bias: {bias_val}A')
    axs[0, 1].set_title('Accuracy (Akurasi)')
    axs[0, 1].legend(loc='upper right', fontsize='small')
    axs[0, 1].grid(True, alpha=0.3)

    # 3. Fidelity
    low_fidelity_signal = np.zeros_like(true_signal)
    low_fidelity_signal[0] = true_signal[0]
    for i in range(1, len(t)):
        low_fidelity_signal[i] = lag_val * true_signal[i] + (1 - lag_val) * low_fidelity_signal[i-1]
    
    axs[1, 0].plot(t, true_signal, 'g', alpha=0.5, label='True')
    axs[1, 0].plot(t, low_fidelity_signal, 'r', linewidth=2, label=f'Lag Factor: {lag_val}')
    axs[1, 0].set_title('Fidelity (Respon)')
    axs[1, 0].legend(loc='upper right', fontsize='small')
    axs[1, 0].grid(True, alpha=0.3)

    # 4. Uncertainty
    noise = np.random.normal(0, noise_val, size=len(t))
    noisy_data = true_signal + noise
    axs[1, 1].plot(t, true_signal, 'g', linewidth=2, label='True')
    axs[1, 1].scatter(t[::5], noisy_data[::5], s=10, c='gray', alpha=0.5, label='Measured')
    axs[1, 1].fill_between(t, true_signal - (noise_val*2), true_signal + (noise_val*2), color='orange', alpha=0.3, label='Uncertainty')
    axs[1, 1].set_title('Uncertainty (Ketidakpastian)')
    axs[1, 1].legend(loc='upper right', fontsize='small')
    axs[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig_sim)
    
    st.info("💡 **Tips:** Geser 'Resolution Step' ke 0.1 untuk melihat bagaimana grafik resolusi menjadi lebih halus mendekati sinyal asli.")
