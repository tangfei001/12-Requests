拓展-Requests中如何获取动态参数的办法

def write(self,bookID):
		with open('bookID','w') as f:
			f.write(str(bookID))

def read(self):
		with open('bookID','r') as f:
			return f.read()
