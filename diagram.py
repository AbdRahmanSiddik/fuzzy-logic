import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np


def create_fuzzy_plot(input_value, membership):
  # Definisi domain
  x = [0, 30, 35, 40, 45, 50]

  # Keanggotaan yang dimodifikasi
  y_minim = [1, 1, 0.5, 0, 0, 0]  # Menurun dari 30 - 40
  y_sedang = [0, 0, 0, 1, 0, 0]  # Naik 35 - 40, Turun 40 - 45
  y_banyak = [0, 0, 0, 0, 1, 1]  # Naik dari 40 - 45

  # Membuat plot
  plt.figure(figsize=(8, 5))
  plt.plot(x, y_minim, label="Minim", marker='o')
  plt.plot(x, y_sedang, label="Sedang", marker='o')
  plt.plot(x, y_banyak, label="Banyak", marker='o')

  # Tambahkan garis vertikal untuk input_value
  plt.axvline(x=input_value, color="red", linestyle="--", linewidth=1, label=f"Input: {input_value}")

  # Tambahkan garis horizontal untuk derajat keanggotaan
  for key, value in membership.items():
      if key == "minim":
          plt.hlines(value, 0, input_value, colors="blue", linestyles="dotted", label=f"{key.capitalize()}: {value}")
      elif key == "sedang":
          plt.hlines(value, 0, input_value, colors="green", linestyles="dotted", label=f"{key.capitalize()}: {value}")
      elif key == "banyak":
          plt.hlines(value, 0, input_value, colors="orange", linestyles="dotted", label=f"{key.capitalize()}: {value}")

  # Pengaturan grafik
  plt.title("Fuzzifikasi Variabel Jumlah Inventory", fontsize=14)
  plt.xlabel("Jumlah", fontsize=12)
  plt.ylabel("µ(Jumlah Inventory)", fontsize=12)
  plt.xticks(np.arange(0, 51, 5))
  plt.yticks(np.arange(0, 1.1, 0.1))
  plt.axhline(0, color="black", linewidth=0.8)
  plt.axvline(0, color="black", linewidth=0.8)
  plt.legend()
  plt.grid(alpha=0.4)

  # Simpan grafik
  file_path = os.path.join("static", "fuzzy_plot.png")
  plt.tight_layout()
  plt.savefig(file_path)
  plt.close()
  return file_path

def create_fuzzy_permin(input_value, membership):
  # Definisi domain
  x = [0, 10, 20, 30, 40, 50]

  # Keanggotaan yang diperbaiki
  y_rendah = [1, 1, 0.5, 0, 0, 0]   # Menurun dari 10 ke 30
  y_sedang = [0, 0, 1, 0.5, 0, 0]   # Naik dari 10 ke 20, turun dari 20 ke 40
  y_tinggi = [0, 0, 0, 0.5, 1, 1]   # Naik dari 20 ke 40, maksimum setelah 40

  # Membuat plot
  plt.figure(figsize=(8, 5))
  plt.plot(x, y_rendah, label="Rendah", marker='o') 
  plt.plot(x, y_sedang, label="Sedang", marker='o')
  plt.plot(x, y_tinggi, label="Tinggi", marker='o')

  # Tambahkan garis vertikal untuk input_value
  plt.axvline(x=input_value, color="red", linestyle="--", linewidth=1, label=f"Input: {input_value}")

  # Tambahkan garis horizontal untuk derajat keanggotaan
  for key, value in membership.items():
      if key == "rendah":
          plt.hlines(value, 0, input_value, colors="blue", linestyles="dotted", label=f"{key.capitalize()}: {value}")
      elif key == "sedang":
          plt.hlines(value, 0, input_value, colors="green", linestyles="dotted", label=f"{key.capitalize()}: {value}")
      elif key == "tinggi":
          plt.hlines(value, 0, input_value, colors="orange", linestyles="dotted", label=f"{key.capitalize()}: {value}")

  # Pengaturan grafik
  plt.title("Fuzzifikasi Variabel Jumlah Permintaan", fontsize=14)
  plt.xlabel("Jumlah", fontsize=12)
  plt.ylabel("µ(Jumlah Permintaan)", fontsize=12)
  plt.xticks(np.arange(0, 51, 5))
  plt.yticks(np.arange(0, 1.1, 0.1))
  plt.axhline(0, color="black", linewidth=0.8)
  plt.axvline(0, color="black", linewidth=0.8)
  plt.legend()
  plt.grid(alpha=0.4)

  # Simpan grafik
  file_path = os.path.join("static", "fuzzy_permin.png")
  plt.tight_layout()
  plt.savefig(file_path)
  plt.close()
  return file_path

def create_fuzzy_output_plot(result):
  # Definisi domain
  x = [0, 10, 25, 40, 50]
  y_no_produksi = [1, 0, 0, 0, 0]
  y_kecil = [0, 1, 0, 0, 0]
  y_sedang = [0, 0, 1, 0, 0]
  y_besar = [0, 0, 0, 1, 0]

  # Membuat plot
  plt.figure(figsize=(8, 5))
  plt.stem(x, y_no_produksi, linefmt="blue", markerfmt="bo", basefmt=" ", label="No Produksi")
  plt.stem(x, y_kecil, linefmt="orange", markerfmt="o", basefmt=" ", label="Kecil")
  plt.stem(x, y_sedang, linefmt="green", markerfmt="o", basefmt=" ", label="Sedang")
  plt.stem(x, y_besar, linefmt="red", markerfmt="o", basefmt=" ", label="Besar")

  # Tambahkan garis horizontal untuk hasil fuzzy
  plt.axhline(result, color="red", linestyle="--", linewidth=1, label=f"Hasil: {result}")

  # Pengaturan grafik
  plt.title("Fuzzifikasi Variabel Jumlah Produksi", fontsize=14)
  plt.xlabel("Jumlah", fontsize=12)
  plt.ylabel("µ(Jumlah Produksi)", fontsize=12)
  plt.xticks(range(0, 51, 10))
  plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])  # Sumbu Y diperluas hingga 1.0
  plt.ylim(0, 1.1)  # Memastikan sumbu Y memiliki ruang yang cukup di atas nilai maksimum
  plt.axhline(0, color="black", linewidth=0.8)
  plt.axvline(0, color="black", linewidth=0.8)
  plt.legend()
  plt.grid(alpha=0.4)

  # Simpan grafik
  file_path = os.path.join("static", "fuzzy_output.png")
  plt.tight_layout()
  plt.savefig(file_path)
  plt.close()
  return file_path
