'''
Nama   : Radhia Aulia Nisa
Nim    : 23343049
Prodi  : Informatika
Matkul : Teknik Komputasi
'''

# Matriks augmented
A = [
    [1, 1, 1, 6],   # x1 + x2 + x3 = 6 #indeks i
    [1, 2, -1, 2],  # x1 + 2x2 - x3 = 2 #indeks j
    [2, 1, 2, 10]   # 2x1 + x2 + 2x3 = 10
]

# Fungsi untuk menampilkan matriks augmented dengan format []
def print_matriks(A):
    for baris in A:
        #menampilkan bentuk matriks sesuai format
        baris_str = "[" + " ".join(f"{int(elemen):2d}" for elemen in baris[:-1]) + " | " + f"{int(baris[-1]):2d}" + "]"
        print(baris_str)
    print()


# Fungsi eliminasi Gauss untuk membuat nol di kiri bawah matriks
def eliminasi_gauss(A):
    n = len(A) #jumlah baris pada matriks A

    print("Matriks sebelum eliminasi:")
    print_matriks(A)
    
    # Eliminasi untuk membuat nol di bawah diagonal utama
    for i in range(n): #i mewakili indeks diagonal utama matriks A
        # Pivoting (memastikan elemen diagonal utama tidak nol)
        if A[i][i] == 0: #memeriksa elemen pada diagonal utama A adalah nol, maka baris akan ditukar dengan baris bawahnya
            for j in range(i+1, n): 
                #i=>indeks yg sedang diproses, j=>indeks untuk baris di bawah baris i
                #mencari baris di bawah baris i (baris j) yang memiliki elemen non-nol (tidak nol) //mengeliminasi dari atas ke bawah
                if A[j][i] != 0: #memeriksa apakah baris j memilliki elemen non-nol (tidak nol) di kolom i //jika ada lakukan pertukaran
                    A[i], A[j] = A[j], A[i]  # Tukar baris
                    break
        
        # Membuat elemen di bawah pivot menjadi nol
        for j in range(i+1, n): #memproses baris-baris dibawah baris i
            if A[j][i] != 0:  #memeriksa apakah elemen pada kolom i dan baris j bernilai tidak nol
                faktor = A[j][i] / A[i][i] #menghiitung hasil bagi antara elemen yang ingin di nol kan dengan elemen diagonal menjadikan nol
                for k in range(i, n+1): #melakukan operasi baris utk setiap elemen agar elemen pada posisi A[i][j] menjadi nol
                    A[j][k] = A[j][k] - faktor * A[i][k] #mengurangi setiap elemen pada baris j dengan elemen yg sesuai dari baris i yg dikalikan dgn faktor

        print(f"Matriks setelah membuat nol di kolom {i+1}:")
        print_matriks(A)

# Fungsi substitusi balik untuk mencari nilai variabel
def substitusi_balik(A):  
    n = len(A)  # Mendapatkan jumlah baris (atau kolom, karena matriks ini adalah matriks persegi) dari matriks A.

    x = [0] * n  # Membuat list x yang berisi n elemen, semuanya diinisialisasi dengan nilai 0.
                # List ini akan menyimpan solusi dari sistem persamaan linear.

    for i in range(n-1, -1, -1):  
        # Looping mundur dari indeks n-1 sampai 0 (termasuk). Ini adalah langkah substitusi mundur.
        # Mulai dari persamaan terakhir hingga persamaan pertama.

        x[i] = (A[i][n] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
        # Menghitung nilai x[i] dengan mengurangi jumlah perkalian elemen A[i][j] dan x[j]
        # untuk j > i (nilai-nilai yang sudah dihitung di iterasi sebelumnya), dari A[i][n] 
        # (elemen di sisi kanan dari persamaan ke-i). Setelah itu dibagi dengan A[i][i] 
        # untuk mendapatkan solusi x[i].

    return x  
    # Mengembalikan list x yang berisi solusi dari sistem persamaan linear.


# Jalankan eliminasi Gauss
eliminasi_gauss(A)

# Lakukan substitusi balik dan tampilkan hasil
solusi = substitusi_balik(A)
print(f"Nilai akhir: x1 = {solusi[0]}, x2 = {solusi[1]}, x3 = {solusi[2]}")


