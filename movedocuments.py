import os
import shutil
 
#想要移动文件所在的根目录
rootdir="H:\\Graudate\\image\sebs_lang\\reMOD09A1\\reMOD09A1_B02"
#获取目录下文件名清单
list=os.listdir(rootdir)
#print(list)
 
#移动图片到指定文件夹
#for j in range(20):
    #year= j + 2001
    #print(year)
#for i in range(0,len(list)):     #遍历目录下的所有文件夹
	#path=os.path.join(rootdir,list[i])    
	#print(path)
a=0
b=46
while b < 921:
    for i in range(a,b):
        print(list[i])
    
    a += 46
    b += 46
    print(a,b)
    dirname=os.path.join("H:\\Graudate\\image\\sebs_lang\\reMOD09A1\\reMOD09A1_B02",list[i]) #将根目录与文件夹名连接起来，获取文件目录
	full_path=os.path.join(dirname,item) #将文件目录与文件名连接起来，形成原来完整路径
    
'''
    if os.path.isdir(path):		 #判断是否为文件夹
		for item in os.listdir(path): #遍历该文件夹中的所有文件
			dirname=os.path.join("H:\\Graudate\\image\\sebs_lang\\reMOD09A1\\reMOD09A1_B02",list[i]) #将根目录与文件夹名连接起来，获取文件目录
			full_path=os.path.join(dirname,item) #将文件目录与文件名连接起来，形成原来完整路径
			#des_path="E:/BaiduNetdiskDownload/jaffedbase/resize128_out/1.image"  #目标路径
			#shutil.move(full_path,des_path)  #移动文件到目标路径
			print(full_path)
			#print(des_path)	
'''



