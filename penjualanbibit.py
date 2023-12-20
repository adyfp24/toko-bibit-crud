import os
import json
import getpass

os.system("cls")
data=[]
FILE_JSON='dataTransaksi.json'


def akun(a):
    data=[]
    data=load(FILE_JSON)
    data1=[]
    data1=load("login.json")
    log = False
    if a == "1":
        a1 = input("name : ")
        a2 = input("pass : ")
        for i in data1:
            if i["nama"] == a1 and i["pass"] == a2:
                log = True
        if log:
            for i in range(10):
                os.system("clear")
                menu()
                choice2 = input("Pilih :")
                if choice2 == "1":
                    os.system("cls")
                    tunjukkan_hasil()

                elif choice2 == "2":
                    os.system("cls")   
                    print('Silahkan Melakukan pembelian')
                    tambah()
                
                elif choice2 == "3":
                    os.system("cls")
                    tunjukkan_hasil()
                    hapus()
                    
                elif choice2 == "4":
                    os.system("cls")
                    tunjukkan_hasil()
                    bayar()  

                elif choice2 == "5":
                    os.system("cls")
                    exit()

                elif choice2 == "6":
                    Save(FILE_JSON,data)
                
                else:
                    print("Tidak Valid")
                if i == 9:
                    os.system("clear")
                    print("Anda sudah melebihi batasan transaksi, silahkan login kembali\n")
                    akun("1")
                konf=input("tekan enter untuk kembali")
        else:
            print("akun belum terdaftar\n")
            a = input("apakah anda ingin daftar terlebih dahulu? [y/n] : ")
            if a == "y":
                akun("2")
            elif a == "n":
                print("[1] login\n[2] reg\n[3] exit")
                data=load(FILE_JSON)
                a = input("--> ")
                akun(a)

    elif a == "2":
        a1 = input("name : ")
        a2 = input("pass : ")
        data1.append({
                "nama": a1,
                "pass": a2,
                })
        Save("login.json",data1)
        print('Silahkan login ulang')
        akun("1")
    elif a == "3":
        pass
    else:
        print("Tidak valid\n")
        print("[1] login\n[2] reg\n[3] exit")
        # data=load(FILE_JSON)
        a = input("--> ")
        akun(a)

def menu ():
    print('Selamat datang di Toko Bibit Cabai Verdy')
    print('='*74)
    print('[1] Keranjang bibit')
    print('[2] Beli bibit')
    print('[3] Hapus Transaksi')
    print('[4] Pembayaran')
    print('[5] keluar')
    print("[6] Simpan data")
    print('='*74)


def tambah():
    print("Silahkan pilih bibit yang anda butuhkan")
    print('='*74)
    print('List harga bibit cabai')
    harga=['[1] 1/4 kg = 25000',
    '[2] 1/2 kg = 50000',
    '[3] 2/3 kg = 65000',
    '[4] 1 kg = 100000']
    print(harga)
    print("[0] Cabai Keriting")
    print("[0] Cabai Merah")
    print("[0] Cabai Hijau")
    print("[0] Cabai Rawit")
    nama = input("Masukkan/ketik Jenis Cabai: ")
    id_game= input("Nama petani : ")
    jumlah = int(input("berapa kg(masukkan sesuai nomor list) : "))
    if jumlah==1:
        data.append({
            "nama": nama,
            "id game": id_game,
            "jumlah": "1/4",
            "harga": 25000,
            })
    elif jumlah==2:
        data.append({
            "nama": nama,
            "id game": id_game,
            "jumlah": "1/2",
            "harga": 50000,
            })
    elif jumlah== 3:
        data.append({
            "nama": nama,
            "id game": id_game,
            "jumlah": "2/3",
            "harga": 65000,
            })
    elif jumlah==4:
        data.append({
            "nama": nama,
            "id game": id_game,
            "jumlah": "1",
            "harga": 100000
            })
    else:
        print('Masukkan jumlah bibit(kg) sesuai list')

def hapus():
    print("Nomor urut berapa yang ingin anda hapus  : ")
    x = int(input("Urutan : "))
    data.pop(x-1)

def tunjukkan_hasil():
    print("="*24,"TOKO BIBIT CABAI VERDY","="*25)
    print("="*74)
    print("| %-3s | %-15s | %-15s | %-15s | %-10s |"%("NO", " JENIS CABAI","PETANI", "JUMLAH(kg)", "HARGA"))
    print("="*74)
    for i in range(len(data)):
        print("| %-3s | %-15s | %-15s | %-15s | %-10s |"%(i+1, data[i]["nama"], data[i]["id game"], data[i]["jumlah"], data[i]["harga"]))
        print("| %-3s | %-15s | %-15s | %-15s | %-10s |"%(" ","", " ", " ", " "))
        print("="*74)

def bayar():
    rekening=int(input('masukkan nomor rekening anda :'))
    pin=getpass.getpass('Masukkan PIN anda(6digit): ')
    if len(pin)==6:
        bayar=(input('Masukkan total harga yang mau dibayar :'))
        print(f"Saldo anda berkurang sebesar{bayar}")
        print('=== Pembelian Bibit Sukses ===')

    else:
        print('Masukkan rekening dan PIN anda dengan benar')
def Save(_datars,_data):
        with open(_datars,'w') as output:#w berfungsi untuk menulis ke dalam file json
            output.write(json.dumps(_data))
        print('=== Save Suksessfull ===')
        
def load(_path):
    with open(_path,'r')as output:#r berfungsi untuk membaca data dari output 
        if os.stat(_path).st_size==0:
            return[]
        else:
            _data = json.load(output)
            return _data

print('Selamat datang di Toko Bibit Cabai Verdy')
print('='*74)
print("[1] masuk\n[2] daftar\n[3] keluar")
data=load(FILE_JSON)
a = input("--> ")
akun(a)
