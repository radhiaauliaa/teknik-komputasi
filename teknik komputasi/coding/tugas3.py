'''
Nama   : Radhia Aulia Nisa
Nim    : 23343049
Prodi  : Informatika
Matkul : Teknik Komputasi
'''

# Matriks koefisien utama
a11, a12, a13 = 3, 2, 4
a21, a22, a23 = 1, 1, 1
a31, a32, a33 = 2, -1, 3

# Kolom konstanta
b1, b2, b3 = 3, 2, 3

print("\n\tPROGRAM DETERMINAN")
print("\tRadhia Aulia Nisa")
print("\t    23343049     \n")

# Fungsi untuk menghitung determinan 3x3 dan menampilkan matriks
def determinan3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    print("Determinan:")
    print(f"| {a11:<3} {a12:<3} {a13:<3} |")
    print(f"| {a21:<3} {a22:<3} {a23:<3} |")
    print(f"| {a31:<3} {a32:<3} {a33:<3} |\n")
    
    # Hitung determinan
    det = (a11 * (a22 * a33 - a23 * a32)
           - a12 * (a21 * a33 - a23 * a31)
           + a13 * (a21 * a32 - a22 * a31))
    
    print(f"= {a11} * ({a22} * {a33} - {a23} * {a32}) - {a12} * ({a21} * {a33} - {a23} * {a31}) + {a13} * ({a21} * {a32} - {a22} * {a31})")
    print(f"= {det}\n")
    return det

# Hitung determinan utama (D)
print("1. Determinan Utama (D):")
D = determinan3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)

# Hitung determinan untuk i1 (Di1)
print("2. Determinan untuk i1 (Di1):")
Di1 = determinan3x3(b1, a12, a13, b2, a22, a23, b3, a32, a33)

# Hitung determinan untuk i2 (Di2)
print("3. Determinan untuk i2 (Di2):")
Di2 = determinan3x3(a11, b1, a13, a21, b2, a23, a31, b3, a33)

# Hitung determinan untuk i3 (Di3)
print("4. Determinan untuk i3 (Di3):")
Di3 = determinan3x3(a11, a12, b1, a21, a22, b2, a31, a32, b3)

# Solusi untuk i1, i2, dan i3
i1 = Di1 / D
i2 = Di2 / D
i3 = Di3 / D

print("\nHasil:")
print("Nilai i1:", i1)
print("Nilai i2:", i2)
print("Nilai i3:", i3)
