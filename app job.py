import gradio as gr

# Fungsi yang akan memproses teks dari inputan pengguna di web
def deteksi_loker(teks_input):
    if not teks_input.strip():
        return "Masukkan teks lowongan terlebih dahulu."
        
    # Ubah input pengguna jadi angka pakai vectorizer yang sama dengan saat training
    teks_vec = vectorizer.transform([teks_input])
    
    # AI memberikan tebakan (0 atau 1) dan persentase probabilitasnya
    hasil_prediksi = model.predict(teks_vec)[0]
    probabilitas = model.predict_proba(teks_vec)[0]
    
    prob_asli = probabilitas[0] * 100
    prob_palsu = probabilitas[1] * 100
    
    # Logika untuk menampilkan hasil ke layar web dengan alasan keyakinan
    if hasil_prediksi == 1:
        analisis = (
            f"⚠️ HATI-HATI! Loker ini terindikasi PALSU / PENIPUAN.\n\n"
            f"📊 Alasan Analisis Keyakinan AI:\n"
            f"- Probabilitas Palsu: {prob_palsu:.2f}% (Tinggi)\n"
            f"- Probabilitas Asli: {prob_asli:.2f}%\n\n"
            f"Sistem mendeteksi kecenderungan pola kalimat yang sering digunakan oleh penipu, "
            f"seperti meminta biaya pendaftaran, janji gaji tidak realistis, atau prosedur tidak resmi."
        )
        return analisis
    else:
        analisis = (
            f"✅ AMAN. Loker ini terindikasi ASLI.\n\n"
            f"📊 Alasan Analisis Keyakinan AI:\n"
            f"- Probabilitas Asli: {prob_asli:.2f}% (Tinggi)\n"
            f"- Probabilitas Palsu: {prob_palsu:.2f}%\n\n"
            f"Sistem menilai struktur teks ini aman dan serupa dengan karakteristik penulisan lowongan kerja formal/profesional."
        )
        return analisis

# Membuat kerangka website aplikasi
interface = gr.Interface( 
    fn=deteksi_loker,
    inputs=gr.Textbox(lines=5, placeholder="Paste teks lowongan di sini... (misal: syarat kerja, cara daftar, dll)"),
    outputs=gr.Textbox(label="Hasil Analisis AI & Alasan Keyakinan"),
    title="Pendeteksi Loker Palsu (Anti-Scam) 🔎",
    description="Sistem Machine Learning untuk mendeteksi indikasi penipuan pada lowongan pekerjaan beserta alasan analisisnya."
)

# Menjalankan aplikasi web
interface.launch(share=True)
