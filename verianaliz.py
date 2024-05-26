import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def istatistik_ve_gorsellestirme(veri):
    # Veriyi numpy array'e dönüştür
    veri_array = np.array(veri)

    # Veri istatistiklerini hesapla
    ortalama = np.mean(veri_array)
    medyan = np.median(veri_array)
    standart_sapma = np.std(veri_array)
    minimum = np.min(veri_array)
    maksimum = np.max(veri_array)

    # Veriyi pandas DataFrame'e dönüştür
    veri_df = pd.DataFrame(veri_array, columns=['Değerler'])

    # Histogram çizimi
    plt.hist(veri_array, bins=20, color='skyblue', edgecolor='black')
    plt.title('Veri Histogramı')
    plt.xlabel('Değerler')
    plt.ylabel('Frekans')

    # Ortalama, medyan, standart sapma, minimum ve maksimum değerleri çizime ekle
    plt.axvline(ortalama, color='red', linestyle='dashed', linewidth=1,
                label=f'Ortalama: {ortalama:.2f} ({np.sum(veri_array == ortalama)})')
    plt.axvline(medyan, color='green', linestyle='dashed', linewidth=1,
                label=f'Medyan: {medyan:.2f} ({np.sum(veri_array == medyan)})')
    plt.axvline(standart_sapma, color='orange', linestyle='dashed', linewidth=1,
                label=f'Standart Sapma: {standart_sapma:.2f} ({np.sum(veri_array == standart_sapma)})')
    plt.axvline(minimum, color='purple', linestyle='dashed', linewidth=1,
                label=f'Minimum Değer: {minimum:.2f} ({np.sum(veri_array == minimum)})')
    plt.axvline(maksimum, color='brown', linestyle='dashed', linewidth=1,
                label=f'Maksimum Değer: {maksimum:.2f} ({np.sum(veri_array == maksimum)})')
    plt.legend()

    plt.grid(True)
    plt.show()

    # Sonuçları yazdır
    print("İstatistikler:")
    print("Ortalama:", ortalama)
    print("Medyan:", medyan)
    print("Standart Sapma:", standart_sapma)
    print("Minimum Değer:", minimum)
    print("Maksimum Değer:", maksimum)


# Kullanıcıdan veri girişi al
veri = input("Lütfen veriyi virgülle ayırarak girin: ").split(',')
veri = [float(x.strip()) for x in veri]

# İstatistikleri hesapla ve görselleştir
istatistik_ve_gorsellestirme(veri)
