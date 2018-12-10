import os
import face_recognition as fr
import cv2
import time
def recognize():
	c = "attrib -h -s -r /s /d facepath.txt"
	os.system(c)
	fi = open("facepath.txt")
	fp = fi.read()
	fi.close()
	c1 = "attrib +h +s +r /s /d facepath.txt"
	os.system(c1)
	known_image = fr.load_image_file(fp)
	try:
		camera = cv2.VideoCapture(0)
		retval,im=camera.read()
		cv2.imwrite('uk.jpg',im)
		del(camera)
		unknown_image = fr.load_image_file("uk.jpg")
		be = fr.face_encodings(known_image)[0]
		ue = fr.face_encodings(unknown_image)[0]
		r = fr.compare_faces([be],ue)
	except:
		r=[False]
	#print(r[0])
	os.remove("uk.jpg")
	return r[0]

def main_func():
	res = recognize()
	if res == True:
		t=os.path.basename(__file__)
		nli1 = t.split(".")
		#nl12 = t.split("-")
		s,s2="",""
		for i in range(len(nli1)-1):
			s+=nli1[i]
		nli2 = s.split("-")
		s2=nli2[1]
		s3=nli2[0]+"."+s2
		cm = "attrib -h -s -r /s /d "+s3
		cm1 = "attrib +h +s +r /s /d "+s3
		#cm2 = "attrib +h +s +r /s /d "+"facepath.txt"
		os.system(cm) 
		c="start "+s3
		os.system(c)
		os.system(cm1)
	else:
		c = "echo Invalid User!"
		os.system(c)
		time.sleep(5)
main_func()