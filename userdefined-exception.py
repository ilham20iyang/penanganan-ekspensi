import math 

#membuat eksepsi AbstrackError
class AbstractError(RuntimeError)
	def __init__ (self,s):
		self.s = 
#menedefinisikan kelas abstrak
class DuaDimensi(object):
	def __init__(self):
		raise AbstractError("ERROR: " + "DuaDimensi" + "Adalah kelas abstrak")
	def luas(self):
		raise NotImplementedError
	def keliling(self)
		raise NotImplementedError
#membuat kelas lingkaran,
#turunan dari kelas DuaDimensi

class Lingkaran(DuaDimensi):
		def __init__(self.r):
			self.r = r
		def luas(self):
			return math.pi * self.r * self.r
		def keliling(self):
			return 2 * math.pi * self.r

def main():
	#instansiasi kelas Lingkaran : BENAR
	obj1 = lingkaran(3)

	print("LINGKARAN")
	print("luas\t\t:", obj1.luas()) 
	print("keliling\t:",obj1.keliling())

	#instalasi kelas DuaDimensi : SALAH
	try:
		print("nMembuat objek" + "dari kelas DuaDimensi....")
		obj2 = DuaDimensi()
	except AbstractError as error:
		print(error.s)
	else:
		print("DUADIMENSI")
		print("luas\t\t:", obj2.luas())
		print("keliling\t:",obj2.keliling())

if __name__ == '__main__':
	main()
		
		
