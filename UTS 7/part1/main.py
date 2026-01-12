from antrian import *
from controllers import *

while True:
	bersihkan_layar()
	menu()
	pilihan = input_pilihan()
	
	if pilihan == "1":
		tambah_antrian_controller()
	elif pilihan == "2":
		panggil_antrian_controller()
	elif pilihan == "3":
		lihat_antrian_controller()
	elif pilihan == "4":
		print("\nProgram selesai | Terima kasih!")
		break
	else:
		pilihan_tidak_sesuai_controller()
		
	input()
	continue