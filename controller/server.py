# memasukkan library
import paramiko
import os

# memasukkan ip , username , dan password kedua node tersebut
list_ip = ["192.168.2.11","192.168.2.12"]
username = "root"
password = "root"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# menggunakan fungsi satu node, berfungsi untuk menggunakan hanya 1 node untuk
# menampilkan data yang ingin ditampilkan 

# Panggil perNode
def satu_node():
    ip_add = list(map(int, input("Pilih Node : ").split(";")))
    print("\nAnda memilih Node", ip_add)

# memilih opsi bangun datar yang diinginkan
    
    #Pilihan Menu 
    print("1. Menghitung Luas dan Keliling Segitiga")
    print("2. Menghitung Luas dan Keliling Lingkaran")
    print("3. Menghitung Luas dan Keliling Persegi")

    pilih = int(input("\nMasukkan Pilihan : "))
    print()
    #1. Segitiga
    #2. Lingkaran
    #3. Persegi

# pengkondisian untuk menjalankan opsi yang dipilih
    
    if (pilih==1):
        alas = float(input("Input alas : "))
        tinggi = float(input("Input tinggi : "))
        sisi = float(input("Input sisi : "))
        print()
        for ip in ip_add:
            ssh_client.connect(hostname=list_ip[ip-1],username=username,password=password)
            print ("Berhasi Masuk ke {0} (Node {1})".format(list_ip[ip-1], ip))
            hub = ssh_client.get_transport().open_session()
            hub.invoke_shell()
            
            hub.send("cd UAS\n")
            hub.send("python3 segitiga.py\n")
            hub.send(str(alas) + "\n")
            hub.send(str(tinggi) + "\n")
            hub.send(str(sisi) + "\n")
            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
            
    elif (pilih==2):
        jari = float(input("Input jari-jari : "))
        print()
        for ip in ip_add:
            ssh_client.connect(hostname=list_ip[ip-1],username=username,password=password)
            print ("Berhasil Masuk ke {0} (Node {1})".format(list_ip[ip-1], ip))
            hub = ssh_client.get_transport().open_session()
            hub.invoke_shell()
            
            hub.send("cd UAS\n")
            hub.send("python3 lingkaran.py\n")
            hub.send(str(jari) + "\n")
            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
            
    elif (pilih==3):
        sisi = float(input("Input sisi : "))
        print()
        for ip in ip_add:
            ssh_client.connect(hostname=list_ip[ip-1],username=username,password=password)
            print ("Berhasil Masuk ke {0} (Node {1})".format(list_ip[ip-1], ip))
            hub = ssh_client.get_transport().open_session()
            hub.invoke_shell()
            
            hub.send("cd UAS\n")
            hub.send("python3 persegi.py\n")
            hub.send(str(sisi) + "\n")
            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
            
    else:
        print("Maaf pilihan anda tidak tersedia..")



# Panggil semua Node
def all_node():
    #Pilihan Menu
    print("1. Menghitung Luas dan Keliling Segitiga")
    print("2. Menghitung Luas dan Keliling Lingkaran")
    print("3. Menghitung Luas dan Keliling Persegi")

    pilih = int(input("\nMasukkan Pilihan : "))
    print()
    #1. Segitiga
    #2. Lingkaran
    #3. Persegi
    if (pilih==1):
        alas = float(input("Input alas : "))
        tinggi = float(input("Input tinggi : "))
        sisi = float(input("Input sisi : "))
        print()
        pilih=1
        for ip_add in list_ip:
            ssh_client.connect(hostname=ip_add,username=username,password=password)
            print ("Berhasil Masuk ke {0} (Node {1})".format(ip_add, pilih))
            pilih=pilih+1
            hub = ssh_client.get_transport().open_session()

            # seolah-olah user login dengan klien terminal SSH
            
            hub.invoke_shell()

            # data yang ingin dikirim    
            
            hub.send("cd UAS\n")
            hub.send("python3 segitiga.py\n")
            hub.send(str(alas) + "\n")
            hub.send(str(tinggi) + "\n")
            hub.send(str(sisi) + "\n")

            # mengirim data ke controller            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
            
    elif (pilih==2):
        jari = float(input("Input jari-jari : "))
        print()
        pilih=1
        for ip_add in list_ip:
            ssh_client.connect(hostname=ip_add,username=username,password=password)
            print ("Berhasil Masuk ke {0} (Node {1})".format(ip_add, pilih))
            pilih=pilih+1
            hub = ssh_client.get_transport().open_session()
            hub.invoke_shell()
            
            hub.send("cd UAS\n")
            hub.send("python3 lingkaran.py\n")
            hub.send(str(jari) + "\n")
            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
            
    elif (pilih==3):
        sisi = float(input("Input sisi : "))
        print()
        pilih=1
        for ip_add in list_ip:
            ssh_client.connect(hostname=ip_add,username=username,password=password)
            print ("Berhasil Masuk ke {0} (Node {1})".format(ip_add, pilih))
            pilih=pilih+1
            hub = ssh_client.get_transport().open_session()
            hub.invoke_shell()
            
            hub.send("cd UAS\n")
            hub.send("python3 persegi.py\n")
            hub.send(str(sisi) + "\n")
            
            hasil = hub.recv(65535).decode('ascii')
            print(hasil)
    
    else:
        print("Maaf pilihan anda tidak tersedia...")



# Main Menu 
os.system("title Main Menu")

def keluar():
    print("Keluar dari Program? (y/n)", end=" ")
    x = str(input())
    if (x=="y" or x=="Y" or x=="yes"):
        print()
        quit()
    elif (x=="n" or x=="N" or x=="no"):
        menu()

# Fungsi Menu
def menu():
    os.system('cls')
    
    #Menu
    print("================================")
    print("Program Menghitung Luas & Keliling Bangun Datar")
    print("Program yang tersedia ;")
    print("1. Segitiga")
    print("2. Lingkaran")
    print("3. Persegi")
    print("================================")
    
    pilih=0;
    for ip_add in list_ip:
        pilih=pilih+1
        print("Pilihan Node", pilih,"=", ip_add)
        
    print("\n1. Pilih satu Node")
    print("2. Jalankan Semua Node")
    pilih = int(input("\nInput Pilihan : "))
    if (pilih==1):
        satu_node()
    elif (pilih==2):
        all_node()
    else:
        print("Maaf pilihan anda tidak tersedia...")
    keluar()

menu()

