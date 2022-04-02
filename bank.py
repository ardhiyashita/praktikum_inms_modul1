import time
from datetime import datetime
from turtle import update
import mysql.connector #digunakan untuk mengimport library mysql
mydb_local = mysql.connector.connect( #data-data pada variabel ini dikoneksikan menggunakan sintaks mysql.connector.connect()
    host="localhost", #merupakan nama host yang digunakan
    user="root", #merupakan nama user yang digunakan
    passwd="", #diisi apabila terdapat password didalamnya
    database="db_modul1", #merupakan nama database yang digunakan
)

mydb_host = mysql.connector.connect(
    host="db4free.net",
    user="ardhiya",
    passwd="kK3SVnb8DMWSS@-",
    database="db_modul1",
)


mycursor = mydb_local.cursor() #digunakan untuk pengolahan data CRUD yang diambil dari database
mycursor_host = mydb_host.cursor() #digunakan untuk pengolahan data CRUD yang diambil dari database

def read_transaksi(): #digunakan untuk membaca isi dalam tabel
        print("Data Host")
        mycursor_host.execute("select * from tb_transaksi") #digunakan untuk mengeksekusi sintaks sql yang dituliskan
        for i in mycursor_host.fetchall(): #mengambil masing-masing data dengan menggunakan fetch sehingga data tampil per row/baris
            idx = i[0] #karena data yang ditampilkan berupa tupel maka diambil per indeks array untuk mendapatkan data mentah
            pegawai = i[1]
            customer = i[2]
            barang = i[3]
            harga = i[4]
            status_transaksi = i[5]
            tgl_transaksi = i[6]
            updated_at = i[7]
            deleted_at = i[8]
            print(str(idx)+" "+pegawai+" "+customer+" "+barang+" "+str(harga)+" "+str(status_transaksi)+" "+str(tgl_transaksi)+" "+str(updated_at)+" "+str(deleted_at))
            #data mentah (value) kemudian di print sehingga tampil


def update_status_transaksi_trx(): #digunakan untuk mengupdate data transaksi, sama seperti sebelumnya, disini saya mencoba membuat sintaks yang berbeda yaitu dengan menggunakan parameter
    idx = input("Silahkan input id data yang ingin diubah: ")
    update = input("Ubah status_transaksi menjadi (berhasil/gagal): ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #digunakan untuk mengambil waktu saat ini ke dalam bentuk string        
    sql = "update tb_transaksi set updated_at ='"+timestamp+"', status_transaksi ='"+update+"' where id="+idx+" " #digunakan untuk mengupdate data pada tabel transaksi sesuai parameter yang diberikan
    mycursor_host.execute(sql)
    mydb_host.commit()

    sink = "INSERT INTO tb_sync (id_tabel, aksi) VALUES ("+idx+", 'update') " 
    mycursor_host.execute(sink)
    mydb_host.commit()
    print("Berhasil mengupdate transaksi pada db host")


def sync():

    sync = []
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    

    mycursor_host.execute("SELECT * FROM tb_sync WHERE id >=(SELECT MAX(id)-2 FROM tb_sync) AND id <=(SELECT MAX(id) FROM tb_sync)")
    for i in mycursor_host.fetchall():
        idx = i[0]
        id_tabel = i[1]
        aksi = i[2]
        sinkronisasi = i[3]
        sync.append(i)
        # print(sync)

        for i in range(0,3):
            print('.')
            time.sleep(1)

        if str(sinkronisasi) == "None":
                
            
            if aksi == "update":
                mycursor_host.execute("select * from tb_transaksi where id ="+str(id_tabel)+"")
                for i in mycursor_host.fetchall():
                    status = i[5]

                    sql = "update tb_transaksi set updated_at ='"+timestamp+"', status_transaksi ='"+status+"' where id="+str(id_tabel)+" "
                    mycursor.execute(sql)
                    mydb_local.commit()
                    print("Berhasil mengupdate transaksi tabel " +str(id_tabel)+ " pada db local")

                    sinkron = "update tb_sync set sinkronisasi ='telah sinkron' where id="+str(idx)+""
                    mycursor_host.execute(sinkron)
                    mydb_host.commit()

                    mycursor.execute("DELETE FROM tb_sync WHERE id_tabel IS NULL")
                    mydb_local.commit()

            else:
                print("Kesalahan histori sinkronisasi")


        else:
            print("Data " +str(idx)+ " telah tersinkronisasi")
        
            
        
    

sync()
# delete_cache()
# update_status_transaksi_trx()
# read_transaksi()





