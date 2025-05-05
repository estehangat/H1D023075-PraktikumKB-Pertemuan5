import tkinter as tk
from tkinter import messagebox

# Data aturan sistem pakar
def rekomendasi_tanaman(tanah, cahaya, air):
    rules = {
        ("Lempung", "Tinggi", "Banyak"): "Padi, Jagung",
        ("Lempung", "Tinggi", "Sedang"): "Singkong, Kacang Panjang",
        ("Lempung", "Tinggi", "Sedikit"): "Bawang Merah, Cabe Rawit",
        ("Lempung", "Sedang", "Banyak"): "Ubi Jalar, Talas",
        ("Lempung", "Sedang", "Sedang"): "Kacang Tanah, Terong",
        ("Lempung", "Sedang", "Sedikit"): "Tomat, Seledri",
        ("Lempung", "Rendah", "Banyak"): "Pakis, Sirih",
        ("Lempung", "Rendah", "Sedang"): "Mint, Kemangi",
        ("Lempung", "Rendah", "Sedikit"): "Lidah Mertua, Sirih Gading",

        ("Gembur", "Tinggi", "Banyak"): "Jagung Manis, Semangka",
        ("Gembur", "Tinggi", "Sedang"): "Cabai, Terong",
        ("Gembur", "Tinggi", "Sedikit"): "Bawang Daun, Bayam Merah",
        ("Gembur", "Sedang", "Banyak"): "Wortel, Kentang",
        ("Gembur", "Sedang", "Sedang"): "Tomat, Brokoli",
        ("Gembur", "Sedang", "Sedikit"): "Lobak, Sawi",
        ("Gembur", "Rendah", "Banyak"): "Daun Bawang, Seledri",
        ("Gembur", "Rendah", "Sedang"): "Jahe, Kunyit",
        ("Gembur", "Rendah", "Sedikit"): "Sirih Gading, Sansiviera",

        ("Berpasir", "Tinggi", "Banyak"): "Semangka, Melon",
        ("Berpasir", "Tinggi", "Sedang"): "Tomat, Cabe",
        ("Berpasir", "Tinggi", "Sedikit"): "Kaktus, Lidah Buaya",
        ("Berpasir", "Sedang", "Banyak"): "Bayam, Kangkung",
        ("Berpasir", "Sedang", "Sedang"): "Rosmarin, Lavender",
        ("Berpasir", "Sedang", "Sedikit"): "Aloe Vera, Sukulen",
        ("Berpasir", "Rendah", "Banyak"): "Talas Hias, Pakis",
        ("Berpasir", "Rendah", "Sedang"): "Sansevieria, Lidah Mertua",
        ("Berpasir", "Rendah", "Sedikit"): "Kaktus Mini, Sukulen Mini",

        ("Liat", "Tinggi", "Banyak"): "Pisang, Pepaya",
        ("Liat", "Tinggi", "Sedang"): "Jagung, Singkong",
        ("Liat", "Tinggi", "Sedikit"): "Bawang Merah, Cabai Kering",
        ("Liat", "Sedang", "Banyak"): "Bayam, Kangkung",
        ("Liat", "Sedang", "Sedang"): "Terong, Ubi Jalar",
        ("Liat", "Sedang", "Sedikit"): "Daun Mint, Kemangi",
        ("Liat", "Rendah", "Banyak"): "Sirih, Pakis",
        ("Liat", "Rendah", "Sedang"): "Kunyit, Jahe",
        ("Liat", "Rendah", "Sedikit"): "Sansiviera, Sirih Gading",

        ("Gambut", "Tinggi", "Banyak"): "Kelapa, Pisang",
        ("Gambut", "Tinggi", "Sedang"): "Kacang Panjang, Pepaya",
        ("Gambut", "Tinggi", "Sedikit"): "Jagung Manis, Bayam Merah",
        ("Gambut", "Sedang", "Banyak"): "Keladi, Talas",
        ("Gambut", "Sedang", "Sedang"): "Jahe, Kunyit",
        ("Gambut", "Sedang", "Sedikit"): "Tomat, Terong",
        ("Gambut", "Rendah", "Banyak"): "Sirih, Pakis",
        ("Gambut", "Rendah", "Sedang"): "Sansiviera, Sirih Gading",
        ("Gambut", "Rendah", "Sedikit"): "Sukulen, Kaktus Hias"
    }

    return rules.get((tanah, cahaya, air), "Belum ada rekomendasi untuk kombinasi ini.")

# Fungsi untuk menangani tombol submit
def submit():
    tanah = var_tanah.get()
    cahaya = var_cahaya.get()
    air = var_air.get()
    
    if not tanah or not cahaya or not air:
        messagebox.showwarning("Peringatan", "Silakan lengkapi semua pilihan.")
        return

    hasil = rekomendasi_tanaman(tanah, cahaya, air)
    label_hasil.config(text=f"Rekomendasi Tanaman:\n{hasil}")

# GUI
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Tanaman")
root.geometry("400x400")

tk.Label(root, text="Pilih Jenis Tanah:").pack()
var_tanah = tk.StringVar()
tk.OptionMenu(root, var_tanah, "Lempung", "Gembur", "Berpasir", "Liat", "Gambut").pack()

tk.Label(root, text="Pilih Intensitas Cahaya:").pack()
var_cahaya = tk.StringVar()
tk.OptionMenu(root, var_cahaya, "Tinggi", "Sedang", "Rendah").pack()

tk.Label(root, text="Pilih Ketersediaan Air:").pack()
var_air = tk.StringVar()
tk.OptionMenu(root, var_air, "Banyak", "Sedang", "Sedikit").pack()

tk.Button(root, text="Rekomendasikan Tanaman", command=submit).pack(pady=10)

label_hasil = tk.Label(root, text="", font=("Calibri", 12), wraplength=300, justify="center")
label_hasil.pack(pady=20)

root.mainloop()
