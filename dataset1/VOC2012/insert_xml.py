from lxml import etree
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom
XML_DIR = "./Annotations_ori"
files = glob.glob(XML_DIR+"/*.xml")

trainval = []
#print(files)
for f in files:
	tree = ET.parse(f)
	root = tree.getroot()

	for obj in root.findall("object"):
		#name = ET.SubElement(obj,"name")
		obj.find("name").text = "circle"
	tree = ET.ElementTree(root)
	
	with open("./newAnnotations/{}".format(f.split("/")[2]),"wb") as f:
		tree.write(f,encoding="utf-8")
