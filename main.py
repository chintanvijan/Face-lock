import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getfile():
	Tk().withdraw() 
	filename = askopenfilename() 
	return filename

def getuserimage():
	Tk().withdraw() 
	filename = askopenfilename() 
	fi = open("facepath.txt","w")
	fi.write(filename)
	fi.close()

def hide(t):
	c="attrib +h +s +r /s /d "+t
	r=os.system(c)
	nli = t.split(".")
	s,k="",""
	#nli[-2]=nli[-1]+"-"+nli[-2]
	for i in range(len(nli)-1):
		s+=nli[i]
	fmain = open("code.py")
	fr = fmain.read()
	fmain.close()
	fname=s+"-"+nli[-1]+".py"
	fi = open(fname,"w")
	fi.write(fr)
	fi.close()
	f = open("facepath.txt")
	fr1 = f.read()
	f.close()
	nli1=fname.split("\\")
	for i in range(len(nli1)-1):
		k+=nli1[i] 
	ts=k+"facepath.txt"
	print(ts)
	f1 = open(ts,"w")
	f1.write(fr1)
	f1.close()
	#cm = "attrib +h +s +r /s /d "+ts
	#os.system(cm)




