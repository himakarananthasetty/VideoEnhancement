import cv2
#from cv2 import dnn_superres
import numpy as np
import glob
import os
from PIL import Image
from PIL import ImageEnhance
print('enter brightness value')
brightness = float(input())
print('enter color value')
color = float(input())
print('enter sharpness value')
sharpness = float(input())
print('enter contrast value')
contrast=float(input())
print("please wait!!")
#import shutil
#import json
#from matplotlib import pyplot as plt
def brightness_enh(image_file):
    enh_bri = ImageEnhance.Brightness(image_file)
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened
def colour_enh(image_file):
    enh_col = ImageEnhance.Color(image_file)
    image_colored = enh_col.enhance(color)
    return image_colored    
def sharp_enh(image_file):
    enh_sha = ImageEnhance.Sharpness(image_file)
    image_sharped = enh_sha.enhance(sharpness)
    return image_sharped
def contrast_enh(image_file):
    enh_con=ImageEnhance.Contrast(image_file)
    image_contrast =enh_con.enhance(contrast)
    return image_contrast
def retur(image_file):
    return image_file            
vidcap = cv2.VideoCapture('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\vid1.mp4')
success,image = vidcap.read()
count = 0

#sr = dnn_superres.DnnSuperResImpl_create()
os.mkdir('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg')
os.mkdir('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg\\enhh')
os.chdir('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg')  
while success:
  cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1
img_array = []
i=0
a=[]
print('1=brightness')
print('2=color')
print('3=sharpness')
print('4=contrast')
print('0=no change')
print('enter order')
for i in range(4):
    ele=int(input())
    a.append(ele)
dict={
      '0':retur,
      '1':brightness_enh,
      '2':colour_enh,
      '3':sharp_enh,
      '4':contrast_enh
}
print("please wait!")

for filename in glob.glob('*.jpg'):
    image=cv2.imread(filename)
    #blur = cv2.bilateralFilter(image,80,75,75)     #Biliteralfilter

    #cv2.imshow(image)
    #img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    #sr.readModel(filename)
    #sr.setModel("edsr", 3)
    #result = sr.upsample(image)
    im_pil = Image.fromarray(image)
    #image_s1=dict.get(a[0])(im_pil)
    image_s1=dict.get('%d'%a[0])(im_pil)
    image_s2=dict.get('%d'%a[1])(image_s1)
    image_s3=dict.get('%d'%a[2])(image_s2)
    image_sharped=dict.get('%d'%a[3])(image_s3)
   # enh_bri = ImageEnhance.Brightness(im_pil)
    #brightness = 1
    #image_brightened = enh_bri.enhance(brightness)
    #enh_col = ImageEnhance.Color(image_brightened)
   # color = 1.2
   # image_colored = enh_col.enhance(color)
   # enh_con = ImageEnhance.Contrast(image_colored)
   # contrast = 0.5
   # image_contrasted = enh_con.enhance(contrast)
   # enh_sha = ImageEnhance.Sharpness(image_contrasted)
   # sharpness = 2
   # image_sharped = enh_sha.enhance(sharpness)
    image_sharped=np.asarray(image_sharped)
   
    r_image, g_image, b_image = cv2.split(image_sharped)

    r_image_eq = cv2.equalizeHist(r_image)
    r_image_cl = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    r_image_eq = r_image_cl.apply(r_image_eq)
    #g_image_eq = cv2.equalizeHist(g_image)
    #g_image_cl = cv2.createCLAHE(g_image_eq)
    g_image_eq = cv2.equalizeHist(g_image)
    g_image_cl = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    g_image_eq = g_image_cl.apply(g_image_eq)
    #b_image_eq = cv2.equalizeHist(b_image)
    #b_image_cl = cv2.createCLAHE(b_image_eq)
    b_image_eq = cv2.equalizeHist(b_image)
    b_image_cl = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    b_image_eq = r_image_cl.apply(b_image_eq)
    image_eq = cv2.merge((r_image_eq, g_image_eq, b_image_eq))
    blur = cv2.bilateralFilter(image_eq,85,65,55)     #Biliteralfilter
    #blur = cv2.medianBlur(image_eq,7)

    cmap_val = None

    cv2.imwrite('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg\\enhh\\'+ filename,blur)
    i=i+1

i=0

list = os.listdir('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg\\enhh\\') # dir is your directory path
number_files = len(list)
filename='C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imggggg\\enhh\\'
for i in range(number_files) :
    img = cv2.imread(filename+'%i'%i+'.jpg')
    i=i+1
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
   
 
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

#shutil.rmtree('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\img\\enh')import numpy as np