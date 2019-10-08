def main():
	#membuat judul program
	print("PROGRAM PEMBAGIAN BILANGAN")

	#Mendefiniskan blok try..except

	try:
		#meminta user memasukkan bilangan
	a = float (input("Masukkan a: "))
	b = float (input("Masukkan b: "))

	#melakukan pembagian
		hasil = a / b

	#mengintisipasi pembagian dengan 0
	except (ZeroDivisionError, ValueError,keyboardInterrupt):
		print("\nERROR: Anda telah melakukan" + "kesalahan")

	else:
		print("\na : ,a")
		print("b :",b)
		print("a / b = __main__", hasil)
		
	if __name__ == " __main__":
		main()
