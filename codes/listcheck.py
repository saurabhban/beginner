if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores

	query = input("enter the name")

	list1 = list(student_marks[query])
	lenght = len(list1)
	print(list1)
	print(lenght)
	s = sum(list1)
	print(s/lenght)

