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
	ET.SubElement(annotation, "path").text="/home/artic/Desktop/models-master/research/VOCdevkit/"+folder+"/JPEGImages/"+str(name)
	source=ET.SubElement(annotation, "source")
	ET.SubElement(source, "database").text="Unknown"
	size=ET.SubElement(annotation, "size")
	ET.SubElement(size, "width").text=str(img_width)
	ET.SubElement(size, "height").text=str(img_height)
	ET.SubElement(size, "depth").text=str(3)
	ET.SubElement(annotation, "segmented").text=str(0)
	return annotation


def create_circle(img,nums,annotaion):
	for i in range(0 ,nums):
		# x_min=random.randint(0, img_width-50)
		# y_min=random.randint(0, img_width-50)
		x_min = random.randrange(0, img_width - 50,2)
		y_min=random.randrange(0, img_width-50,2)

		x_max=random.randrange(x_min+50, img_width,2)
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
		# print('x_min:{}'.format(x_min))
		# print('y_min:{}'.format(y_min))
		# print('x_max:{}'.format(x_max))
		# print('y_max:{}'.format(y_max))
		# print('center_x:{}'.format(center_x))
		# print('center_y:{}'.format(center_y))
		# print('r:{}'.format(r))

		fill_percentage = random.randint(0,100)
		if fill_percentage >=20:
			cv2.circle(img,(int(center_x),int(center_y)), int(r), (red,green,blue),-1)
		else:
			cv2.circle(img, (int(center_x), int(center_y)), int(r), (red, green, blue), 2)
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

mode = ['normal','gauss','gauss_more']
j =0
for m in mode:
	for f_name in range(0,34):
		f_name = f_name + 34*j
		img = np.zeros((512,512,3), np.uint8)
		col_random = random.randint(0, 255)
		print(random.randint(0, 255))


		row, col, ch = img.shape


		annotation=ET.Element("annotation")
		file_name = str(f_name) +"_" + str(m)
		img.fill(100)
		# pts = np.array([[0,0],[0,512],[512,512],[512,0]])
		# pts = np.array([[0,0],[0,512],[512,512],[512,0]])
		# img = cv2.fillPoly(img,pts=[pts],color=(200,200,0))
		annotation=create_xml(annotation,file_name+".jpg")

		annotation=create_circle(img,random.randint(1, 4),annotation)
		if m == 'gauss':
			img= cv2.imread("./"+folder+"/JPEGImages/"+str(f_name)+"_normal.jpg")
			# img = cv2.medianBlur(img,3)
			mean = 0
			var = 0.1
			sigma = 30
			gauss = np.random.normal(mean,sigma,(row,col,ch))
			gauss = gauss.reshape(row,col,ch)

			gauss_img = img - gauss
			print(img.shape)
			print(gauss.shape)
			print(gauss)
			print(img)
			img = gauss_img

		if m == 'gauss_more':
			img = cv2.imread("./" + folder + "/JPEGImages/" + str(f_name) + "_normal.jpg")p
			print('gauss_more')
			# img = cv2.medianBlur(img,3)
			mean = 0
			var = 0.1
			sigma = 60
			gauss = np.random.normal(mean,sigma,(row,col,ch))
			gauss = gauss.reshape(row,col,ch)

			gauss_img = img + gauss
			print(img.shape)
			print(gauss.shape)
			print(gauss)
			print(img)
			img = gauss_img



		tree = ET.ElementTree(annotation)
		tree.write("./"+folder+"/Annotations/"+str(file_name)+".xml")
		cv2.imwrite("./"+folder+"/JPEGImages/"+str(file_name)+".jpg",img)
	j +=1
		#cv2.imshow('image',img)
		#cv2.waitKey(0)
