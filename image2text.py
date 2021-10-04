#Image to text
import pytesseract
import cv2
#import re
def image2text():
    img = cv2.imread('image.png')
    height,width,channels = img.shape

    img = img[int(height/4):int(height/2),0:int(width/2)]

    cv2.imwrite("img.png", img)

    text = pytesseract.image_to_string(img,lang="mc")
    if "XYZ" in text:
        #extract only the xyz
        text = text.split('\n')
        for i in range(len(text)):
            if "XYZ" in text[i]:
                return(text[i])    
    else:
        return("I'm sorry, my developer is shit, can't do more than this, maybe this useless cropping could give ya a helping hand, idk man")
