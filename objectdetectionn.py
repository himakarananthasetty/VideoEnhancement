import cv2
vidcap = cv2.VideoCapture('C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\imgggg\\su.mp4')
vidcap.set(3,640)
vidcap.set(4,480)

thres= 0.5
classNames= []
classFile ='C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\Object_Detection_Files\\coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n') 

configPath = 'C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\Object_Detection_Files\\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'C:\\Users\\vedav\\Desktop\\INTERNSHIP\\DRDL internship\\DRDO\\Object_Detection_Files\\frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0 / 127.5)
net.setInputMean(list([127.5,127.5,127.5]))
net.setInputSwapRB(True)

while True:
    success,vidcap=vidcap.read()
    classIds , confs ,bbox = net.detect(vidcap,confThreshold=thres)
    print(classIds,bbox)
    
    if len(classIds) !=0:
        for classId , confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(vidcap,box,color=(0,255,0),thickness=3)
            cv2.putText(vidcap,classNames[classId-1].upper()(box[0]+10,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(vidcap,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            
        
    
    cv2.waitkey(1)