# membuat program kasir resto sederhana
def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
     
    else:
        print('input program salah harap ulangi')
 
def kasir():
    # masukan input dari user
    print('MENU')
    print('HARGA')
    print(' ')
    print('MENU')
    print('HARGA')
    print(' ')
    print('MENU')
    print('HARGA')
    print(' ')
    print('MENU')
    print('HARGA')
    print(' ')
    print('MENU')
    print('HARGA')
    print(' ')
    print('MENU')
    print('HARGA')
    print(' ')
    nama_barang = input('masukan pesanan: ')
    harga = int(input('harga: '))
    jumlah_beli = int(input('jumlah: '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
        tanya()
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()
 
 
def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'NAMA BISNIS', '=' * 10)
    print('APLIKASI KASIR')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. PROGRAM KASIR')
    print('2. KELUAR')
 
    # input pilihan
    pilihan = input('pilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        kasir()
    else:
        print('KELUAR')
        exit()
 
 
# membuat fungsi authentifikasi sederhana
def get_login():
    print('=' * 20)
    print('NAMA BISNIS')
    print('Silahkan login')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
    
    if username == 'admin' and password == 'admin':
        print(f'Selamat datang {username}')
        main_menu()
    else:
        print('Login gagal')
        print('Silahkan cek kembali username dan password anda')
        get_login()
 
def tanya():
    tanya = input('ketik "hitung" untuk menghitung lagi, dan ketik "menu" untuk ke menu)')
    if tanya == 'menu':
        main_menu()
    elif tanya == 'hitung':
        kasir()
    else:
        print('input salah')
        print('masukan input dengan benar')
 
 #main program
if __name__=='__main__':
    get_login()
