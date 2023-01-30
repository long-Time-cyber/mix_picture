#at least 2 pictures with the same size

import os
import cv2

#注意使用\\，并且目录中要求不能出现中文
folder = 'D:\\Python_project\\draw_a_picture_by_AI\\image_file'
os.chdir(folder)
images = []
for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        file_path = os.path.join(folder, filename)
        image = cv2.imread(file_path)
        images.append(image)
result = cv2.addWeighted(images[0], 0.5, images[1], 0.5, 0)
cv2.imwrite('result.jpg', result)
