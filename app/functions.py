import cv2
import string
import pytesseract
import config

class functions:

    def initiate(self):
        pytesseract.pytesseract.tesseract_cmd = config.tesseract_path
    
    def draw_boxes_on_text(self,img):
        raw_data = pytesseract.image_to_data(
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        )
        for count, data in enumerate(raw_data.splitlines()):
            if count > 0:
                data = data.split()
                if len(data) == 12:
                    x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                    cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 1)
                    cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255) , 1)
                
        return img

    def process(self,img_path):
        img = cv2.imread(img_path)
        w,h = img.shape[1],img.shape[0]

        ratio = w//config.maxlen
        w = w//ratio
        h = h//ratio

        img = cv2.resize(
            img,
            (w,h),
            interpolation=cv2.INTER_AREA
        )

        return draw_boxes_on_text(img)