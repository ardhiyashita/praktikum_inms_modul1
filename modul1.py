from datetime import datetime
from sqlite3 import Timestamp  #digunakan untuk mengimport library datetime
import mysql.connector #digunakan untuk mengimport library mysql
mydb_local = mysql.connector.connect( #data-data pada variabel ini dikoneksikan menggunakan sintaks mysql.connector.connect()
    host="localhost", #merupakan nama host yang digunakan
    user="root", #merupakan nama user yang digunakan
    passwd="", #diisi apabila terdapat password didalamnya
    database="db_modul1", #merupakan nama database yang digunakan
)

mydb_host = mysql.connector.connect( #data-data pada variabel ini dikoneksikan menggunakan sintaks mysql.connector.connect()
    host="192.168.1.3", #merupakan nama host yang digunakan
    user="admin123", #merupakan nama user yang digunakan
    passwd="", #diisi apabila terdapat password didalamnya
    database="db_modul1", #merupakan nama database yang digunakan
)

mycursor = mydb_local.cursor() #digunakan untuk pengolahan data CRUD yang diambil dari database
mycursor_host = mydb_host.cursor() #digunakan untuk pengolahan data CRUD yang diambil dari database

def read_transaksi(): #digunakan untuk membaca isi dalam tabel
        print("Data Local")
        mycursor.execute("select * from tb_transaksi") #digunakan untuk mengeksekusi sintaks sql yang dituliskan
        for i in mycursor.fetchall(): #mengambil masing-masing data dengan menggunakan fetch sehingga data tampil per row/baris
            idx = i[0] #karena data yang ditampilkan berupa tupel maka diambil per indeks array untuk mendapatkan data mentah
            pegawai = i[1]
            customer = i[2]
            barang = i[3]
            harga = i[4]
            tgl_transaksi = i[5]
            updated_at = i[6]
            status_transaksi = i[7]
            print(str(idx)+" "+pegawai+" "+customer+" "+barang+" "+str(harga)+" "+str(tgl_transaksi)+" "+str(updated_at)+" "+str(status_transaksi))    
            #data mentah (value) kemudian di print sehingga tampil
        
        
        print("-----------------------------------")
        print("Data Host")
        mycursor_host.execute("select * from tb_transaksi") #digunakan untuk mengeksekusi sintaks sql yang dituliskan
        for i in mycursor_host.fetchall(): #mengambil masing-masing data dengan menggunakan fetch sehingga data tampil per row/baris
            idx = i[0] #karena data yang ditampilkan berupa tupel maka diambil per indeks array untuk mendapatkan data mentah
            pegawai = i[1]
            customer = i[2]
            barang = i[3]
            harga = i[4]
            tgl_transaksi = i[5]
            updated_at = i[6]
            status_transaksi = i[7]
            print(str(idx)+" "+pegawai+" "+customer+" "+barang+" "+str(harga)+" "+str(tgl_transaksi)+" "+str(updated_at)+" "+str(status_transaksi))
            #data mentah (value) kemudian di print sehingga tampil

# ---------------------- INSERT DATA ----------------------
def insert_transaksi(): #digunakan untuk menginput data transaksi
    print("Input data transaksi. Isilah data-data berikut") #seperti biasa menggunakan pertanyaan untuk pengisian data.
    pegawai = input("pegawai : ") #variabel akan mengampung data (value) yang nantinya akan diinput ke database
    customer = input("customer : ")
    barang = input("barang : ")
    harga = int(input("harga : "))
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = "insert into tb_transaksi(pegawai, customer, barang, harga, tgl_transaksi, updated_at, status_transaksi) values (%s, %s, %s, %s, %s, %s, %s)" #variabel yang menampung sintaks sql yang cukup panjang    
    val = (pegawai, customer, barang, harga, timestamp, "Null", "pending") #variabel akan melempar value agar masuk ke dalam sintaks diatasnya, karena banyak jadi saya pisahkan

    # ---------------------- LOCAL DATA ----------------------
    mycursor.execute(sql, val) #seperti biasa mycursor.execute() digunakan untuk mengeksekusi sintaks dari bahasa sql yang dituliskan di python
    mydb_local.commit() #commit() digunakan ketika kita memodifikasi data tabel baik dalam create, update, delete

    # ---------------------- HOST DATA ----------------------
    mycursor_host.execute(sql, val) #seperti biasa mycursor.execute() digunakan untuk mengeksekusi sintaks dari bahasa sql yang dituliskan di python
    mydb_host.commit() #commit() digunakan ketika kita memodifikasi data tabel baik dalam create, update, delete
    print("Berhasil menambah transaksi")

# ---------------------- UPDATE DATA ----------------------
def update_transaksi(idx, kolom, data_baru): #digunakan untuk mengupdate data transaksi, disini saya mencoba membuat sintaks yang berbeda yaitu dengan menggunakan parameter
    if kolom == "pegawai" or "customer" or "barang" or "harga": #digunakan sebagai pemilihan pada kolom yang bersesuaian pada tabel tb_transaksi
        sql = "update tb_transaksi set "+kolom+" ='"+data_baru+"' where id="+idx+" " #digunakan untuk mengupdate data pada tabel transaksi sesuai parameter yang diberikan
        mycursor.execute(sql)
        mydb_local.commit()

        mycursor_host.execute(sql)
        mydb_host.commit()
        print("Berhasil mengubah data transaksi")
    else:
        print("Nama kolom salah! Perhatikan kembali nama kolom pada database!")

def update_status_transaksi_trx(): #digunakan untuk mengupdate data transaksi, sama seperti sebelumnya, disini saya mencoba membuat sintaks yang berbeda yaitu dengan menggunakan parameter
    idx = input("Silahkan input id data yang ingin diubah: ")
    update = input("Ubah status_transaksi menjadi (berhasil/gagal): ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #digunakan untuk mengambil waktu saat ini ke dalam bentuk string        
    sql = "update tb_transaksi set updated_at ='"+timestamp+"', status_transaksi ='"+update+"' where id="+idx+" " #digunakan untuk mengupdate data pada tabel transaksi sesuai parameter yang diberikan
    mycursor.execute(sql)
    mydb_local.commit()

    mycursor_host.execute(sql)
    mydb_host.commit()
    print("Berhasil mengubah data transaksi")

# ---------------------- DELETE DATA ----------------------
def delete_data(): #digunakan untuk menghapus data
    idx = input("Pilih id dari data yang ingin dihapus : ") #digunakan sebagai id sesuai untuk data yang akan dihapus
    tanya = input("Yakin menghapus data (Y/N) ? ") #digunakan untuk memastikan apakah benar-benar ingin menghapus data
    if tanya == "Y":
        sql = "delete from tb_transaksi where id="+idx+" " #apabila telah yakin maka sintaks ini akan menghapus data yang berseuaian dengan apa yang diinputkan sebelumnya
        mycursor.execute(sql)
        mydb_local.commit()

        mycursor_host.execute(sql)
        mydb_host.commit()
        print("Berhasil menghapus data pada tb_transaksi ")
    elif tanya == "N": #digunakan untuk membatalkan penghapusan data
        print("Penghapusan dicancel/batal")
    else: #dibuat apabila terdapat salah penginputan
        print("Pilihan tidak sesuai! Silahkan coba lagi")
    

# insert_transaksi()

# update_transaksi("2", "barang", "tabanan")
# update_status_transaksi_trx()
# read_transaksi()
delete_data()





