from os import listdir
from os.path import isfile, join
open('aeroplane_train.txt', 'w').close()
mypath="../../JPEGImages/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
with open("aeroplane_train.txt", "a") as f:
	f.truncate()
	for fi in onlyfiles:
		s=str(fi)
		f.write("%s\n" % (s[:-4]))
		print(s[:-4])
