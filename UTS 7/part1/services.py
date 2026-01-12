from constants import *

def tambah_antrian_service(orang):
	antrian.append(orang)
	
def hapus_antrian_service():
	orang = antrian.pop(0)
	return orang