import requests
import os
import base64
import cv2
import json
import numpy as np
def get_requests(url,image_path):
    with open(image_path, 'rb') as f:
            image_bytes = base64.b64encode(f.read())
    f.close
    img = str(image_bytes,'utf-8')
    data = {"img":img}
    #发送请求
    resp = requests.post(url, json=data)
    get_json = resp.json()
    view_base64 = get_json["image_view_base64"]
    return view_base64
def base64_to_image(base64_code):
 # base64解码
 img_data = base64.b64decode(base64_code)
 # 转换为np数组
 img_array = np.frombuffer(img_data, np.uint8)
 # 转换成opencv可用格式
 img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
 return img
