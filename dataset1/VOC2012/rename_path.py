from lxml import etree
import glob
import os
import shutil
XML_DIR = "./Annotations"
files = glob.glob(XML_DIR+"/*.xml")

trainval = []

for f in files:
	#shutil.copy(f,"./newAnnotations/{}".format(f.split("/")[2]))
	print("./newAnnotations/{}".format(f.split("/")[2]))
	print(f.split("/")[2].split(".")[0])
	#print(f.split("/")[2])
	tree = etree.parse(f)
	#print(tree.find("filename").text)
	#print(tree.find("filename").text.split(".")[0]+".xml")
	
	tree.find("path").text = "/home/artic/Desktop/models-master/research/VOCdevkit_small/VOC2012/JPEGImages/{}.jpg".format(f.split("/")[2].split(".")[0])
	with open("./newAnnotations/{}".format(tree.find("filename").text.split(".")[0]+".xml"),"wb") as f:
		f.write(etree.tostring(tree,xml_declaration=False,encoding="utf-8"))
