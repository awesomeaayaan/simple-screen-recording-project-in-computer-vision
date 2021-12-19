#screen recoder
import cv2 as c
import pyautogui as p #pyautogui is used to capture the screen resolution
import numpy as np

#create resolution
rs = p.size()#it will capture the size of the screen resolution

#filename in which we store recording
fn = input("please enter any file name and path")#give a path where you want to save your screen record
 
#fix the frame rate
fps = 60.0 #if fps is less the video will be slow and if we take large value then the video play will be fast

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create a recording module
c.namedWindow("Live_recording",c.WINDOW_NORMAL)#it will name the window 
c.resizeWindow("Live_recording",(600,400)) #it will resize the window size

while True:
    img = p.screenshot()#pyautogui take a screen shot and save it into an array
    f = np.array(img)#screen shot from the above are store in the array 
    f = c.cvtColor(f,c.COLOR_BGR2RGB)#open cv always read the image in BGR and here we convert bgr color to rgb
    output.write(f)# it is used to save the recording screen
    c.imshow("Live_recording",f)#is used to display output
    
    if c.waitKey(1) == ord("q"):#it is used to exit the video by simply pressing the q key
        break
    
output.release()#when everything done it will release the video capture object
c.destroyAllWindows()#it will closes all the open frames
       

