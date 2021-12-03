import sys
sys.path.append('..')
from get_post import get_requests
from get_post import base64_to_image
import cv2
url = 'http://ai.7tyun.com:7006/AI/image/liquid/level'
image_path = './test.png'
image_view_base64 = get_requests(url,image_path)
image = base64_to_image(image_view_base64)
cv2.imwrite('image.jpg',image)
cv2.namedWindow('image',0)
cv2.imshow('image',image)
cv2.waitKey(0)