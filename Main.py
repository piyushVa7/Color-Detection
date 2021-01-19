import cv2
import numpy as np
import pandas as pd

image_path=input("Enter the image name \n") #Enter the name of the image (if in same folder if not then the address too)
clicked = False
r = g = b = xpos = ypos = 0
image = cv2.imread(image_path)        #using opencv to read the image 


labels=["color","color_name","hex","R","G","B"]               #reading colors from the colorslist
csv = pd.read_csv('colors_list.csv', names=labels, header=None)


def getColorName(R,G,B):  #function to get the most matching color
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def draw_function(event, x,y,flags,param):  #to get the coordinates of mouse click
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):
    cv2.imshow("image",image)
    if (clicked):
        text = getColorName(r,g,b) 
        cv2.putText(image, text,(xpos,ypos),2,0.8,(255,255,255),2,cv2.LINE_8) #For darker colors
        if(r+g+b>=600):
            cv2.putText(image, text,(xpos,ypos),2,0.8,(0,0,0),2,cv2.LINE_8) #For lighter colors
        clicked=False            

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()