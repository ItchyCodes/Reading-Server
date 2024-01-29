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
    print("capturing image...")
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv.png', image)
    del(camera)
    return image

def refinenum(num):
    print("refining number...")
    front = num[2:]
    end = front[:len(front)-2]
    return end


def everything():
    captureimage()
    image_path = 'opencv.png'
    text = read_text(image_path)
    refinedtext = refinenum(text)
    os.remove(image_path)
    return text, refinedtext

