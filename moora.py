import numpy as np
import pandas as pd

# Fungsi untuk normalisasi matriks
def normalisasi(matrix):
    """
    Fungsi untuk menormalisasi matriks berdasarkan akar kuadrat total kuadrat pada kolom.
    """
    normal_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    return normal_matrix

# Fungsi untuk menghitung nilai MOORA
def hitung_moora(matrix, tipe_kriteria):
    """
    Menghitung nilai optimasi MOORA.
    
    Parameters:
    - matrix: Matriks normalisasi.
    - tipe_kriteria: List untuk menentukan kriteria (1 = Benefit, 0 = Cost).
    
    Returns:
    - Hasil optimasi MOORA.
    """
    benefit = matrix[:, tipe_kriteria == 1].sum(axis=1)  # Menjumlahkan kriteria benefit
    cost = matrix[:, tipe_kriteria == 0].sum(axis=1)    # Menjumlahkan kriteria cost
    
    hasil_moora = benefit - cost  # Selisih antara benefit dan cost
    return hasil_moora

# Fungsi utama
def main():
    # Dataset untuk pengujian (contoh data)
    # Baris = alternatif, Kolom = kriteria
    data = np.array([
        [8, 5, 6, 7],   # Alternatif 1
        [6, 8, 7, 6],   # Alternatif 2
        [7, 7, 8, 5],   # Alternatif 3
        [9, 6, 7, 8]    # Alternatif 4
    ])
    
    # Tipe kriteria: 1 = Benefit, 0 = Cost
    tipe_kriteria = np.array([1, 0, 1, 1])  # Benefit-Cost-Benefit-Benefit
    
    # Menampilkan dataset awal
    print("Dataset Awal:")
    print(pd.DataFrame(data, columns=["Kriteria 1", "Kriteria 2", "Kriteria 3", "Kriteria 4"]))
    
    # Normalisasi data
    print("\nMatriks Normalisasi:")
    matriks_normal = normalisasi(data)
    print(pd.DataFrame(matriks_normal, columns=["Kriteria 1", "Kriteria 2", "Kriteria 3", "Kriteria 4"]))
    
    # Menghitung nilai MOORA
    hasil_moora = hitung_moora(matriks_normal, tipe_kriteria)
    
    # Membuat ranking berdasarkan nilai MOORA
    ranking = np.argsort(hasil_moora)[::-1]  # Urutan indeks dari terbesar ke terkecil
    print("\nHasil Perangkingan MOORA:")
    for i, idx in enumerate(ranking):
        print(f"Peringkat {i+1}: Alternatif {idx+1} dengan nilai {hasil_moora[idx]:.4f}")
    
    # Menentukan alternatif terbaik
    alternatif_terbaik = ranking[0] + 1
    print(f"\nAlternatif terbaik adalah Alternatif {alternatif_terbaik}")

if __name__ == "__main__":
    main()
