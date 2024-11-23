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
    n = len(A)

    print("Matriks sebelum eliminasi:")
    print_matriks(A)
    
    # Eliminasi untuk membuat nol di bawah diagonal utama
    for i in range(n): 
        if A[i][i] == 0: 
            for j in range(i+1, n): 
                if A[j][i] != 0: 
                    A[i], A[j] = A[j], A[i]  
                    break
        
        for j in range(i+1, n): 
            if A[j][i] != 0:  
                faktor = A[j][i] / A[i][i] #melakukan perbandingan dengan elemen pivot

#A[2][0]= 2
#---------- = 2
#A[0][0]= 1

                for k in range(i, n+1): 
                    A[j][k] = A[j][k] - faktor * A[i][k] 

        print(f"Matriks setelah membuat nol di kolom {i+1}:")
        print_matriks(A)

# Fungsi substitusi balik untuk mencari nilai variabel
def substitusi_balik(A):  
    n = len(A) 

    x = [0] * n  
            
    for i in range(n-1, -1, -1):  
        x[i] = (A[i][n] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]

    return x  

eliminasi_gauss(A)

solusi = substitusi_balik(A)
print(f"Nilai akhir: x1 = {solusi[0]}, x2 = {solusi[1]}, x3 = {solusi[2]}")


