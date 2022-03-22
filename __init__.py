import os

class fotpy():
	def write(filePath,rawData):
		try:
			file = open(filePath,"w")
			file.write(rawData)
		except FileNotFoundError as e:
			raise('WrongFilePath: Path given was wrong')
	
	def read(filePath):
		try:
			file = open(filePath,"r")
			text = file.read()
			return text
		except FileNotFoundError as e:
			raise('WrongFilePath: Path given was wrong')
	
	def appendF(filePath,rawData):
		try:
			file = open(filePath,"a")
			toWrite = f"\n{rawData}"
			file.write(toWrite)
		except:
			raise('CodeError: Somthing went wrong')
	
	def delF(filePath):
		try:
			os.remove(filePath)
		except:
			raise('CodeError: Somthing went wrong')
	
	def mkF(filePath):
		try:
			os.mkdir(filePath)
		except:
			raise('CodeError: Something went wrong')
