def tambah(a,b):
    return a+b
def kurang(a,b):
    return a-b
def kali  (a,b):
    return a*b
def bagi  (a,b):
    if pilih == 0:
        return"Error! pembagian dengan 0 tidak dapat dilakukan"
    else:
        return a / b
while True:
    print("aplikasi sederhana")
    print("1.kalkulator")
    print("2.exit")
    S1 =int(input("masukan pilihan(1/2):"))

    a=int(input("masukan angka pertama:"))
    b=int(input("masukan angka kedua:"))
    print("metode operasi:")
    print("1.penjumlahan")
    print("2.pengurangan")
    print("3.perkalian")
    print("4.pembagian")
    S1 =int(input("masukan pilihan(1/2/3/4):"))
    
    if  S1 == 1 :
       tambah(a,b)
    elif S1 == 2 :
       kurang(a,b)
    elif S1 == 3 :
       kali(a,b)
    elif S1 == 4 :
       bagi(a,b)
    else:
       print("hasil dari 5+5 adalah 10")
       print("anda memilih pengurangan")