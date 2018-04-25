def doSomething():
	a = [4, 7, 12, 0, 1, 3, 8]
	print("doing something")
	print(a)
	i = 0
	while i < len(a):
		j=i+1
		while j < len(a):
			if a[j] < a[i]:
				a[i], a[j] = a[j], a[i]
			j+=1
		i+=1
	print(a)

doSomething()

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i,j in enumerate(a):
	print("index: ", i) #index
	print("value: ", j) #list value


print() 
i = 0
for j in a:
	print("index: ", i)
	print("value: ", j)
	i+= 1

	

