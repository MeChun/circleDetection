for i in range(1472, 9675):
    with open("trainval.txt", "a") as f:
		f.write("%s\n" % (i))
		print(i)
