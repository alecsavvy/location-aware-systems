def sum_all(lst):
	def add(x, y):
		return x + y
	return reduce(add, lst)
	
def sum_all2(lst):
	return reduce(lambda x, y: x + y, lst)

print "sum_all without lambda", sum_all([1,2,3,4])	
print "sum_all with lambda", sum_all2([1,2,3,4])