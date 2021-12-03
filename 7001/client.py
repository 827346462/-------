import sys
sys.path.append('..')
from get_post import get_requests
from get_post import base64_to_image
import cv2
#url = 'http://ai.7tyun.com:8887/AI/image/pointMeter/circle'
url = 'http://ai.7tyun.com:7002/AI/image/digit'
image_path = './test1.png'
image_view_base64 = get_requests(url,image_path)
image = base64_to_image(image_view_base64)
cv2.namedWindow('image',0)
cv2.imshow('image',image)
cv2.waitKey(0)