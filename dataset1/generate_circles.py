import numpy as np
import cv2
import random
import math
import xml.etree.cElementTree as ET

img_width=512
img_height=512

folder="VOC2007"

def create_xml(annotation,name):
	annotation=ET.Element("annotation")
	ET.SubElement(annotation, "folder").text=folder
	ET.SubElement(annotation, "filename").text=str(name)
	ET.SubElement(annotation, "path").text="/home/artic/Desktop/circle_detection/dataset/VOCdevkit/"+folder+"/"+str(name)+".jpg"
	source=ET.SubElement(annotation, "source")
	ET.SubElement(source, "database").text="unknown"
	size=ET.SubElement(annotation, "size")
	ET.SubElement(size, "width").text=str(img_width)
	ET.SubElement(size, "height").text=str(img_height)
	ET.SubElement(size, "depth").text=str(3)
	ET.SubElement(annotation, "segmented")
	return annotation


def create_circle(img,nums,annotaion):
	for i in range(0 ,nums):
		x_min=random.randint(0, img_width-50)
		y_min=random.randint(0, img_width-50)

		x_max=random.randint(x_min+50, img_width)
		y_max=y_min+(x_max-x_min)
		
		red=random.randint(0, 255)
		green=random.randint(0, 255)
		blue=random.randint(0, 255)

		while y_max>img_height:
			x_max=random.randint(x_min+50, img_width)
			y_max=y_min+(x_max-x_min)

		center_x=x_min+(x_max-x_min)/2
		center_y=y_min+(y_max-y_min)/2

		r=(y_max-y_min)/2


		cv2.circle(img,(center_x,center_y), r, (red,green,blue),-1)
		#cv2.rectangle(img, (x_min,y_min), (x_max,y_max), (0,0,255), 1)


		object1=ET.SubElement(annotation, "object")
		ET.SubElement(object1, "name").text="circle"
		ET.SubElement(object1, "pose").text="Unspecified"
		ET.SubElement(object1, "truncated").text="0"
		ET.SubElement(object1, "difficult").text="0"
		box=ET.SubElement(object1, "bndbox")
		ET.SubElement(box, "xmin").text=str(x_min)
		ET.SubElement(box, "ymin").text=str(y_min)		
		ET.SubElement(box, "xmax").text=str(x_max)
		ET.SubElement(box, "ymax").text=str(y_max)
	return annotation

for f_name in range (1,200):
	img = np.zeros((512,512,3), np.uint8)
	img.fill(random.randint(0, 255))
	annotation=ET.Element("annotation")

	
	annotation=create_xml(annotation,f_name)
	
	annotation=create_circle(img,random.randint(1, 2),annotation)

	tree = ET.ElementTree(annotation)
	tree.write("./"+folder+"/Annotations/"+str(f_name)+".xml")
	cv2.imwrite("./"+folder+"/JPEGImages/"+str(f_name)+".jpg",img)
	#cv2.imshow('image',img)
	#cv2.waitKey(0)
