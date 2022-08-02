# import library
import streamlit as st
import textwrap as tw
from PIL import Image
import pandas as pd


# Icon header
st.set_page_config(
    page_title="Hashing",
    page_icon= "🖥️",
)

# Content
# Panjang texxt wrapper
Wrap = tw.TextWrapper(width=100)

#  Judul
Title = "HASHING"
iconHeader = "#️⃣"
st.title(f"{iconHeader} {Title.upper()}")

# Sub_judul_1
Sub_judul_1 = "Pengertian Hash"
st.subheader(Sub_judul_1.title())

#  Isi sub_judul_1
Isi_1 = """Hash adalah algoritma yang mengubah data informasi berupa huruf, angka, atau karakter lain menjadi kode alfanumerik dengan ukuran yang tetap melalui fungsi hash yang tidak bisa dikembalikan pada data yang asli. Hash adalah sidik jari atau rangkuman dari data digital."""
image_1 = Image.open(r"images/Hash.jpeg")
st.image(image_1, caption='Pengertian hash', width=700)
for Isi_sub_judul_1 in Wrap.wrap(text=Isi_1):
    st.write(Isi_sub_judul_1)

# Sub_judul_2
Sub_judul_2 = "Perbedaan Hash Dengan Enkripsi"
st.subheader(Sub_judul_2.title())

#  Isi sub_judul_2
Perbedaan = pd.DataFrame({
    'Hash' : [
        "Prosesnya melibatkan pengubahan informasi menjadi nilai tetap yang lebih pendek.", 
        "Setelah hashing, karakter tidak dapat dibaca dan panjangnya tetap.", 
        "lebih aman."],
    'Enkripsi' : [
        "Proses melibatkan pengkodean data sehingga hanya entitas yang berwenang yang dapat menguraikan pesan.", 
        "Setelah enkripsi, karakter tidak dapat dibaca dan panjangnya tidak tetap.", 
        "Amankan tetapi kunci pribadi harus tetap dirahasiakan"]
}, index=[1, 2, 3])
st.dataframe(Perbedaan, 800, None)

# Sub_judul_3
Sub_judul_3 = "Pengertian Hashing"
st.subheader(Sub_judul_3.title())

#  Isi sub_judul_3
Isi_3 = """Hashing adalah proses perubahan data yang akan direpresentasikan ke dalam kode alfanumerik dengan menggunakan rumus matematika yang disebut hash function. Hashing ini merupakan fungsi kriptografi satu arah. Contoh dari algoritma hashing ada SHA1, SHA224, SHA256, SHA384, and SHA512 atau yang sering disebut MD5."""
for Isi_sub_judul_3 in Wrap.wrap(text=Isi_3):
    st.write(Isi_sub_judul_3)

# Sub_judul_4
Sub_judul_4 = "Cara Kerja Hashing"
st.subheader(Sub_judul_4.title())

#  Isi sub_judul_4
Isi_4 = """Hashing pada dasarnya adalah fungsi kriptografi satu arah. Karena hash tidak dapat diubah, mengetahui output dari metode hashing tidak memungkinkan Anda untuk membuat ulang konten file. Namun, itu memungkinkan Anda untuk menilai apakah dua file serupa tanpa mengetahui isinya. Akibatnya, konsep hash didasarkan pada asumsi bahwa hasilnya unik. Kami akan mengalami "tabrakan" jika dua file terpisah menghasilkan intisari yang sama, dan kami tidak dapat menggunakan hash sebagai identifikasi file yang dapat dipercaya. Mempertimbangkan bahwa tidak ada batasan jumlah pasangan kunci/nilai, fungsi hash dapat digunakan untuk memetakan kunci ke ukuran tabel, sehingga membuat nilai hash menjadi indeks untuk elemen tertentu."""
image_2 = Image.open(r"images/Hashing.jpeg")
st.image(image_2, caption='Cara kerja hashing', width=700)
for Isi_sub_judul_4 in Wrap.wrap(text=Isi_4):
    st.write(Isi_sub_judul_4)

#  Isi sub_judul_3
Isi_3 = """Hashing adalah proses perubahan data yang akan direpresentasikan ke dalam kode alfanumerik dengan menggunakan rumus matematika yang disebut hash function. Hashing ini merupakan fungsi kriptografi satu arah. Contoh dari algoritma hashing ada SHA1, SHA224, SHA256, SHA384, and SHA512 atau yang sering disebut MD5."""
for Isi_sub_judul_3 in Wrap.wrap(text=Isi_3):
    st.write(Isi_sub_judul_3)

# Sub_judul_5
Sub_judul_5 = "Manfaat Hashing"
st.subheader(Sub_judul_5.title())

#  Isi sub_judul_5
Isi_5 = {
    "Menjadi Label dan Identitas Bukti Digital": "Hash dapat membantu dalam penyimpanan bukti-bukti digital, ini biasanya diaplikasikan dalam ranah hukum. Karena mampu memberikan kemungkinan identik sampai 99%, hash kerap dipakai untuk keperluan forensik.",
    "Normalisasi Panjang Data yang Beragam" : "Data seperti password memiliki panjang yang berbeda-beda, tergantung dari masing-masing pengguna. Untuk keperluan penyimpanan di database, panjang data sebaiknya diseragamkan. Password tadi disimpan dalam bentuk hash di dalam database sehingga panjang datanya seragam.",
    "Mempercepat Proses Pengiriman" : "Fungsi hash kerap digunakan untuk mengirim message digest dari arsip, ini dapat menghemat proses pengiriman karena pengguna tidak perlu mengirim seluruh salinan dari komputer server",
    "Menjaga Integritas Data" : "Manfaat yang terakhir dari hash adalah menjaga integritas data, khususnya untuk data-data yang sensitif. Ini mencegah para hacker mendapatkan data yang asli.",
    "Validasi Pesan atau Berkas" : "Hasil dari hash function atau digest dapat digunakan sebagai suatu bentuk ‘tanda-tangan’. Dengan membubuhkan nilai hash pada suatu berkas, penerima berkas dapat mengetahui apakah berkas tersebut sudah diubah atau tidak. Penerima akan melakukan hashing pada berkas tersebut dan melakukan pengecekan apakah nilainya sama dengan nilai hash yang dibubuhkan sebagai tanda-tangan. Jika sama, kemungkinan berkasnya tidaklah diubah.",
    "Mengamankan Password" : "Password tidak boleh disimpan dalam bentuk teks asli (plaintext). Jika terjadi kebocoran data, bisa jadi sangat berbahaya. Hash ini digunakan pada password untuk menyamarkan password tersebut kalau-kalau terjadi kebocoran data. Data yang bocor hanyalah digest dari password tersebut dan jika dilakukan dengan benar, akan sulit untuk mengembalikannya ke bentuk teks asli. Mengamankan password ini tidak akan berhasil jika kamu menggunakan algoritma hash yang lemah seperti MD5. Penyebabnya adalah sudah banyak alat yang dapat digunakan hacker untuk mengembalikan hash MD5 ke bentuk aslinya. Contohnya dengan menggunakan rainbow table."
}
image_3 = Image.open(r"images/Manfaat.jpeg")
st.image(image_3, caption='Manfaat Hashing', width=700)
idx = 0
for j in Isi_5:
    idx+=1
    data_5 = Isi_5[j]
    st.write(f"**{idx}. {j}**: {data_5}")

#  Daftar pustaka
Daftar = "Daftar Pustaka"
st.subheader(Daftar.title())
Dapus = [
    "Jola Andrew. 2021. Defenition Hashing . https://www.techtarget.com/searchdatamanagement/definition/hashing (diakses tanggal 1 Agustus 2022)",
    "Steadfastit.com. 2022. What is Hashing in Cyber Security? . https://www.steadfastit.com/resources/blog/managed-it-services/what-is-hashing-in-cyber-security/ (diakses tanggal 1 Agustus 2022)",
    "Kurniawan Bayu. 2022. Hash Adalah: Pengertian, Cara Kerja, Jenis, Fungsi dan Manfaatnya . https://ilmuelektro.id/hash-adalah/ (diakses tanggal 1 Agustus 2022)",
    "Kutu.dev. 2020. Mengenal Hashing, Fungsi Satu Arah . https://kutu.dev/artikel/mengenal-hashing (diakses tanggal 1 Agustus 2022)",
    "Tudor Dora. 2021. What Is Hashing and How Does It Work? . https://heimdalsecurity.com/blog/what-is-hashing/ (diakses tanggal 1 Agustus 2022)",
    "Rezkitha, D. 2021 . Apa itu Hashing dan Bagaimana Cara Kerjanya? . https://pintu.co.id/academy/post/apa-itu-hashing-dan-bagaimana-cara-kerjanya (diakses tanggal 1 Agustus 2022)",
    "Nurul Ramdan. 2018 . Perbedaan Enkoding,Enksripsi, dan Hash. https://medium.com/@ramdannur/perbedaan-enkoding-enkripsi-dan-hash-9f9670767fa3 (diakses tanggal 1 Agustus 2022)"
]
for index in range(len(Dapus)):
    st.write(f"{index+1}. {Dapus[index]}")
