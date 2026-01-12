from services import *
from predicates import *

def tambah_antrian_controller():
	orang = input("masukan nama : ")
	tambah_antrian_service(orang)

def panggil_antrian_controller():
	if apakah_antrian_kosong():
		print("antrian kosong ")
		return
	orang = hapus_antrian_service()
	print(orang)
	
	
def lihat_antrian_controller():
	if apakah_antrian_kosong():
		print("antrian kosong ")
		return
	nomor = 1
	for orang in antrian:
		print(nomor, orang)
		nomor = nomor+1
	
def pilihan_tidak_sesuai_controller():
	print("pilihan tidak tersedia")