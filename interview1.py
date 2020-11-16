import json

import numpy as np
import cv2 

def read_json(path):
    fw = open(path,'r')
    new_dict = json.loads(fw.read())
    target_list = new_dict["boxes"]
    for target in target_list:
        if target["name"]=="box_b":
            print(target['rectangle'])
            right = target['rectangle']['right_bottom'][0]
            bottom = target['rectangle']['right_bottom'][1]
            left = target['rectangle']['left_top'][0]
            top = target['rectangle']['left_top'][1]
 
    return right, left, top, bottom

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='图片拼接')
    parser.add_argument('--json_path',default='C:/Users/Administrator/Downloads/boxes.json', type=str, help='json文件路径')
    parser.add_argument('--image1_path', default='C:/Users/Administrator/Downloads/电池.jpg', type=str, help='任意一张图像')
    parser.add_argument('--image2_path', default='C:/Users/Administrator/Downloads/变压器.jpg', type=str, help='被填充的图像')
    args = parser.parse_args()
    json_path = args.json_path
    image1_path = args.image1_path
    image2_path = args.image2_path
    right, left, top, bottom = read_json(json_path)
    w, h = right - left  , bottom - top
   
    img1 = cv2.imdecode(np.fromfile(image1_path,dtype=np.uint8),-1)
    img2 = cv2.imdecode(np.fromfile(image2_path,dtype=np.uint8),-1)
    img1 = cv2.resize(img1,(w,h),interpolation=cv2.INTER_CUBIC) 
    # 替换
    img2[top:bottom,left:right] = img1
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
    
    

