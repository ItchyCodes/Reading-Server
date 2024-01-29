import cv2
import easyocr
import os

# read image
image_path = 'stopsign2.png'

#img = cv2.imread(image_path)


def read_text(path):
    # instance detector
    print("creating reader...")
    reader = easyocr.Reader(['en'])

    # detect text on image
    print("identifying text...")
    text = reader.readtext(path, detail = 0)

    return text

def captureimage():
    # capture the image from camera
    print("capturing image...")
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()

    # add image to folder to reference later
    cv2.imwrite('opencv.png', image)

    # stop the recording of camera
    del(camera)
    
    return image

def refinenum(num):
    # gets rid of brackets and quotes around number
    print("refining number...")
    front = num[2:]
    end = front[:len(front)-2]
    
    return end


def everything():
    # runs the captureimage() method to take and analyze the image
    captureimage()

    # uses the method read_text() to read the text from the image
    image_path = 'opencv.png'
    text = read_text(image_path)

    # uses the method refinenum() to get rid of brackets
    refinedtext = refinenum(text)

    # remove the image from the folder
    os.remove(image_path)
    
    return text, refinedtext

