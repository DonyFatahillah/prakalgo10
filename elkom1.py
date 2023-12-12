import os
import json
import time

dataMahasiswa = []

fileName = "data_userr.json"

def clear():
    os.system('cls' if os.name == "nt" else "clear")

try:
    with open(fileName, 'r') as file:
        dataMahasiswa = json.load(file)
    print("sukses load data")
    clear()
except (FileNotFoundError, json.JSONDecodeError):
    print("file tidak ditemukan atau data tercorrupt, memakai list kosong.")

def inputData(): 
        print("[1]. Input Data")   
        nama = input("Masukan Nama Mahasiswa : ")
        prak1 = int(input("Masukan Nilai Praktikum 1 : "))
        prak2 = int(input("Masukan Nilai Praktikum 2 : "))
        prak3 = int(input("Masukan Nilai Praktikum 3 : "))
        dataUser = {"nama": nama, "prak1": prak1, "prak2": prak2, "prak3": prak3}
        dataMahasiswa.append(dataUser)
        return clear(), main()
        

def viewData():
    print("[2]. View Data")
    print(" NO.  |   NAMA   | PRAK1  | PRAK2  | PRAK3  |")
    print("======================================================")
    for idx, user in enumerate(dataMahasiswa, start=1):
        print(" {} | {} | {} | {} | {} |".format(
            str(idx).ljust(4),
            user["nama"].ljust(8),
            str(user["prak1"]).ljust(6),
            str(user["prak2"]).ljust(6),
            str(user["prak3"]).ljust(6)
        ))
            
    opsi = input("keluar? (y/n) : ").lower()
    if opsi in ("yes", "y"):
         return clear(),main()
    else:
        return viewData()   

def rataRata():
    while True:
        print("[3]. Nilai Rata Rata Mahasiswa")
        for user in dataMahasiswa:
            rata_rata = (user["prak1"] + user["prak2"] + user["prak3"]) / 3
            print("Rata-rata nilai {} adalah: {}".format(user["nama"], rata_rata))
            
        opsi = input("keluar? (y/n) : ").lower()
        if opsi in ("yes", "y"):
            return clear(),main()
        else:
            continue

def rataRataPrak():
    print("[4]. Rata Rata Nilai Praktikum")
    total_prak1 = sum(user["prak1"] for user in dataMahasiswa)
    total_prak2 = sum(user["prak2"] for user in dataMahasiswa)
    total_prak3 = sum(user["prak3"] for user in dataMahasiswa)
    jumlah_data = len(dataMahasiswa)

    if jumlah_data > 0:
        rata_rata_prak1 = total_prak1 / jumlah_data
        rata_rata_prak2 = total_prak2 / jumlah_data
        rata_rata_prak3 = total_prak3 / jumlah_data
        print(f"Rata Rata Praktikum 1 : {rata_rata_prak1}")
        print(f"Rata Rata Praktikum 2 : {rata_rata_prak2}")
        print(f"Rata Rata Praktikum 3 : {rata_rata_prak3}")
    else:
        print("Tidak ada data mahasiswa.")

    return main()

def rataRataTiapMahasiswa():
    print("[5]. Rata Rata Tiap Mahasiswa")
    nama = input("Masukan Nama : ")
    userFound = False
    for user in dataMahasiswa:
        if user['nama'] == nama:
            userFound = True
            rata_rata = ((user["prak1"] + user["prak2"] + user["prak3"]) / 3 )
            print("rata rata {} adalah {}".format(user["nama"],rata_rata))
            return main()
    if not userFound:
        print("Data Tidak valid")
        return rataRataTiapMahasiswa()

def updateNilai():
    print("[6]. Update Nilai ")
    nama = input("Masukan Nama : ")
    userFound = False
    for user in dataMahasiswa:
        if user['nama'] == nama:
            opsi = input("Praktikum yang akan di edit : ")
            if opsi == "1":
                nilai = input("Masukan Nilai : ")
                user['prak1'] = int(nilai)
                return main()
            elif opsi == "2":
                nilai = input("Masukan Nilai : ")
                user['prak2'] = int(nilai)
                return main()
            elif opsi == "3":
                nilai = input("Masukan Nilai : ")
                user['prak3'] = int(nilai)
                return main()
            else:
                print("opsi tidak valid")
                return updateNilai()
    if not userFound:
        print("Nama Tidak ditemukan!")
        return updateNilai()
    
def deleteUser():
    print("[7]. Hapus User")
    nama = input("Masukan Nama : ")
    userFound = False
    for user in dataMahasiswa:
        if user['nama'] == nama:
            userFound = True
            print(f"{nama} berhasil ditemukan")
            opsi = input(f"Hapus Data dari {nama}? (y/n) : ").lower()
            if opsi in ("y", "yes"):
                dataMahasiswa.remove(user)
                print("Data Berhasil di Hapus")
                return main()
            elif opsi in ("n", "no"):
                return deleteUser()
    if not userFound:
        print("Nama tidak ditemukan")
        return main()

def main():
    while True:
        print("\nPROGRAM LIST")
        print("1. Input Data")
        print("2. View Data")
        print("3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa")
        print("4. Hitung Nilai Rata-Rata Tiap Praktikum")
        print("5. Menghitung Rata Rata Tiap Mahasiswa")
        print("6. Update Nilai Mahasiswa")
        print("7. Hapus User")
        print("8. Save Data")
        print("0. Exit")
        opsi = (input("Masukan Opsi : "))

        if opsi == "1":
            clear()
            inputData()
            return exit
        elif opsi == "2":
            clear()
            viewData()
            return exit
        elif opsi == "3":
            clear()
            rataRata()
            return exit
        elif opsi == "4":
            clear()
            rataRataPrak()
            return exit
        elif opsi == "5":
            clear()
            rataRataTiapMahasiswa()
            return exit
        elif opsi == "6":
            clear()
            updateNilai()
            return exit
        elif opsi == "7":
            clear()
            deleteUser()
            return exit
        elif opsi == "8":
            with open(fileName, "w") as file:
                json.dump(dataMahasiswa, file)
            print("sukses menyimpan data")
            return time.sleep(3),clear(),main()
        elif opsi == "0":
            with open(fileName, "w") as file:
                json.dump(dataMahasiswa, file)
            print("sukses menyimpan data")
            clear()
            return exit
        else:
            break

if __name__ == "__main__":
    clear()
    main()
