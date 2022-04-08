import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

myconfig = r'--oem 3 --psm 11'

img = cv2.imread('test.png')
height, width, channels = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=pytesseract.Output.DICT)

amount_of_boxes = len(data['text'])
for i in range(amount_of_boxes):
    if float(data['conf'][i]) > 60:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(data['text'])
