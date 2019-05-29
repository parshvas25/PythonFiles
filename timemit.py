from timeit import timeit

SIZES = [200,2000,20000,200000,400000000]

def length(size):
	list1 = []
	count = 0
	while count < size:
		list1.append(2)
		count +=1
	return list1

def test_time():
	for size in SIZES:
		list2 = length(size)
		index = size //2
		time = 0
		time += timeit('list2.insert(size,67)', number = 1, globals = locals())
		print("List of size {} took {}".format(size,time))