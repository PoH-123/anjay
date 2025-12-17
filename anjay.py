import datetime
import random
import time
import sys

def animate_text(text, delay=0.03):
    """Animasi pengetikan teks"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def garis_pembatas():
    """Membuat garis pembatas yang menarik"""
    print("=" * 60)

def loading_animation():
    """Animasi loading"""
    animation = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for i in range(15):
        sys.stdout.write(f"\rMenganalisis data {animation[i % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r" + " " * 30)

def main():
    # Header Program
    garis_pembatas()
    print("✨" * 27)
    animate_text("      SELAMAT DATANG DI PROGRAM PROFIL DIGITAL")
    print("✨" * 27)
    garis_pembatas()
    
    time.sleep(1)
    
    # 1. INPUT DATA PENGUNA
    print("\n📝 MASUKKAN DATA DIRI ANDA")
    garis_pembatas()
    
    nama = input("Nama lengkap\t\t: ").title()
    umur_str = input("Umur Anda\t\t: ")
    kota = input("Kota asal\t\t: ").title()
    profesi = input("Profesi saat ini\t: ").capitalize()
    hobi = input("Hobi favorit\t\t: ").capitalize()
    
    # Validasi input umur
    while not umur_str.isdigit() or int(umur_str) <= 0 or int(umur_str) > 120:
        print("❌ Umur tidak valid! Masukkan angka antara 1-120")
        umur_str = input("Umur Anda\t\t: ")
    
    umur = int(umur_str)
    
    # 2. PROSES DATA DAN ANALISIS
    loading_animation()
    
    # Perhitungan dasar
    tahun_sekarang = datetime.datetime.now().year
    bulan_sekarang = datetime.datetime.now().month
    tahun_lahir = tahun_sekarang - umur
    umur_bulan = umur * 12
    umur_hari = umur * 365  # Perkiraan
    
    # Zodiak (sederhana berdasarkan bulan)
    bulan_lahir = random.randint(1, 12)  # Simulasi bulan lahir
    zodiak_list = [
        ("Capricorn", "🪐"), ("Aquarius", "♒"), ("Pisces", "♓"), 
        ("Aries", "♈"), ("Taurus", "♉"), ("Gemini", "♊"),
        ("Cancer", "♋"), ("Leo", "♌"), ("Virgo", "♍"),
        ("Libra", "♎"), ("Scorpio", "♏"), ("Sagittarius", "♐")
    ]
    zodiak, simbol_zodiak = zodiak_list[(bulan_lahir - 1) % 12]
    
    # Generasi berdasarkan tahun lahir
    if tahun_lahir >= 1997 and tahun_lahir <= 2012:
        generasi = "Generasi Z 🎮"
    elif tahun_lahir >= 1981 and tahun_lahir <= 1996:
        generasi = "Milenial 📱"
    elif tahun_lahir >= 1965 and tahun_lahir <= 1980:
        generasi = "Generasi X 📼"
    elif tahun_lahir >= 1946 and tahun_lahir <= 1964:
        generasi = "Baby Boomer 📻"
    else:
        generasi = "Generasi Lainnya 📜"
    
    # Status usia
    if umur < 13:
        kategori_usia = "Anak-anak 👶"
    elif umur < 20:
        kategori_usia = "Remaja 🧑‍🎓"
    elif umur < 40:
        kategori_usia = "Dewasa Muda 👨‍💼"
    elif umur < 60:
        kategori_usia = "Paruh Baya 👨‍🔬"
    else:
        kategori_usia = "Lanjut Usia 👴"
    
    # Fakta unik berdasarkan hobi
    fakta_hobi = {
        "Membaca": "📚 Otak Anda aktif 2x lebih ketika membaca!",
        "Olahraga": "🏃‍♂️ Endorfin meningkat 75% saat berolahraga!",
        "Musik": "🎵 Mendengarkan musik mengurangi stres hingga 65%!",
        "Memasak": "👨‍🍳 80% koki profesional menemukan passion di usia muda!",
        "Programming": "💻 Developer menghabiskan 70% waktu untuk debugging!",
        "Berkebun": "🌱 Tanaman meningkatkan kualitas udara hingga 25%!"
    }
    fakta = fakta_hobi.get(hobi, "🎯 Hobi Anda adalah sumber energi positif!")
    
    # 3. OUTPUT HASIL
    print("\n" + "=" * 60)
    print("🌟" * 27)
    animate_text("           HASIL ANALISIS PROFIL DIGITAL")
    print("🌟" * 27)
    print("=" * 60)
    
    print(f"\n👤 PROFIL SINGKAT")
    print(f"   Nama\t\t: {nama}")
    print(f"   Umur\t\t: {umur} tahun ({umur_bulan} bulan)")
    print(f"   Asal\t\t: {kota}")
    print(f"   Profesi\t: {profesi}")
    print(f"   Hobi\t\t: {hobi}")
    
    print(f"\n📊 ANALISIS USIA")
    print(f"   Tahun Lahir\t: {tahun_lahir}")
    print(f"   Kategori\t: {kategori_usia}")
    print(f"   Generasi\t: {generasi}")
    print(f"   Zodiak\t: {zodiak} {simbol_zodiak}")
    
    print(f"\n🎯 FAKTA MENARIK")
    print(f"   {fakta}")
    
    # Perkiraan masa depan
    print(f"\n🔮 PERKIRAAN MASA DEPAN")
    
    tahun_5 = umur + 5
    tahun_10 = umur + 10
    tahun_20 = umur + 20
    
    milestones = []
    if umur < 18:
        milestones.append(f"🎓 {tahun_lahir + 18}: Kemungkinan lulus SMA")
    if umur < 22:
        milestones.append(f"🎓 {tahun_lahir + 22}: Kemungkinan wisuda kuliah")
    if umur < 30:
        milestones.append(f"💼 {tahun_lahir + 25}: Puncak karir awal")
    if umur < 40:
        milestones.append(f"🏠 {tahun_lahir + 35}: Stabilitas finansial")
    
    for milestone in milestones:
        print(f"   • {milestone}")
    
    # Statistik visual
    print(f"\n📈 VISUALISASI USIA (1 ⬜ = 5 tahun)")
    usia_visual = "⬜" * (umur // 5) + "⬛" * ((100 - umur) // 5)
    print(f"   {usia_visual}")
    print(f"   0{' ' * 18}50{' ' * 18}100 tahun")
    
    # Pesan motivasi
    print(f"\n💫 PESAN MOTIVASI UNTUK {nama.upper()}:")
    motivasi = [
        "Jadilah versi terbaik dari dirimu sendiri!",
        "Setiap langkah kecil membawa pada kesuksesan besar.",
        "Masa depan dimulai dari apa yang kamu lakukan hari ini.",
        "Passion + Konsistensi = Keberhasilan",
        "Usia hanyalah angka, semangatmu yang menentukan!"
    ]
    print(f"   ✨ {random.choice(motivasi)}")
    
    garis_pembatas()
    animate_text("\nTerima kasih telah menggunakan Program Profil Digital!")
    print(f"\nDibuat dengan ❤️ pada {datetime.datetime.now().strftime('%d %B %Y %H:%M:%S')}")
    garis_pembatas()

if __name__ == "__main__":
    main()
