import requests
import os
import base64
import cv2
import json
import numpy as np
def base64_to_image(base64_code):
 # base64解码
 img_data = base64.b64decode(base64_code)
 # 转换为np数组
 img_array = np.frombuffer(img_data, np.uint8)
 # 转换成opencv可用格式
 img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
 return img
def image_to_base64(image_np):
 
 image = cv2.imencode('.jpg',image_np)[1]
 image_code = str(base64.b64encode(image))[2:-1]
 
 return image_code
## 本地读取图片编码进行传递
with open('./result/camera24.jpg', 'rb') as f:
        # image_bytes = f.read()
        image_bytes = base64.b64encode(f.read())
        #image_bytes = image_bytes.decode('ascii')
        #print(image_bytes)
f.close
img = str(image_bytes,'utf-8')
temp = np.load('./result/camera24.npy')
#print(temp)
temp= temp.flatten().tolist()
temp1 = []
temp1.append(temp)
#print(temp1[0])
location = [[69, 135], [68, 229], [113, 230], [115, 141]]
data = {"img":img,"temp":temp,"location":location}
#发送请求
resp = requests.post("http://ai.7tyun.com:5001//AI/image/oil_tank/height", json=data)
get_json = resp.json()
view_base64 = get_json["image_view_base64"]

imgdata = base64.b64decode(view_base64)
# print(type(imgdata.decode()))
# 转换为np数组
img_array = np.frombuffer(imgdata, np.uint8)
# 转换成opencv可用格式
img_np = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)

#img_np = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# img = base64_to_image(view_base64_1)
file = open('./result/1.jpg','wb')
file.write(img_np)
file.close()


