import cv2
import string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Reading image 
img = cv2.imread("img1.jpg")

dim = img.shape
w,h = dim[1],dim[0]

#Width
ratio = w//500
w = w//ratio
h = h//ratio

# Convert to RGB 
img = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (w,h), interpolation = cv2.INTER_AREA)

# Detect texts from image
texts = pytesseract.image_to_string(img)
print(texts)

# conf = r'-c tessedit_char_whitelist='+string.ascii_letters   
conf = r'-c tessedit_char_whitelist='+string.digits
# conf = conf + string.ascii_letters   

def draw_boxes_on_character(img):
    img_width = img.shape[1]
    img_height = img.shape[0]

    # Return each detected character and their bounding boxes.
    boxes = pytesseract.image_to_boxes(img, config =conf)

    print(boxes)
    for box in boxes.splitlines():
        box = box.split(" ")
        character = box[0]
        x = int(box[1])
        y = int(box[2])
        x2 = int(box[3])
        y2 = int(box[4])
        cv2.rectangle(img, (x, img_height - y), (x2, img_height - y2), (0, 255, 0), 1)
        cv2.putText(img, character, (x, img_height -y2), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255) , 1)
    return img

def draw_boxes_on_text(img):
    # Return raw information about the detected texts
    raw_data = pytesseract.image_to_data(img)

    #print(raw_data)
    for count, data in enumerate(raw_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 1)
                cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255) , 1)
                
    return img

# img = draw_boxes_on_character(img)     
img = draw_boxes_on_text(img)   

# show the output
cv2.imshow("Output", img)
cv2.waitKey(0)
