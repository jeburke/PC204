import Week6_1

def area_difference(r1, r2):
	area_r1 = r1.width*r1.height
	area_r2 = r2.width*r2.height
	difference = area_r1 - area_r2
	return difference
def main():
	r1 = Week6_1.create_rectangle(10, 20, 10, 10)
	r2 = Week6_1.create_rectangle(20, 50, 15, 20)
	print area_difference(r1, r2)

if __name__ == '__main__':
	main()
