print("i am going to demostrate jelly bean , jar and crates program")
def jellybean (start_point):
	bean = start_point /2
	carets = bean * 10
	jars = carets *100

	return bean,carets,jars




start_point=1000
bean = start_point*5
carets= start_point/20
jars = start_point/50

bean,carets,jars = jellybean(start_point)

print(f"during the first start point :{start_point}, value of bean,carets and jars are : {bean},{carets} and {jars}")
start_point =start_point / 2
bean,carets,jars = jellybean(start_point)
print(f"during the second start point :{start_point}, value of bean,carets and jars are : {bean},{carets} and {jars}")