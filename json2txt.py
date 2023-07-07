import json
import os
import numpy as np
import cv2 as cv

json_dir = "data/LabelMeJSON"
image_dir = "data/YOLODataset/images/train"
        
items = {
    'tsuyu' : 0,
    'soySauce' : 1,
    'oil' : 2,
    'mirin' : 3
}

def imageDimenstion(image):
    im = cv.imread(image)
    h, w, c = im.shape
    return h, w

def labelme2yolo():
    json_file_names = [filename for filename in os.listdir(json_dir) if filename.endswith('.json')]
    
    
    for filename in json_file_names:
        name = os.path.splitext(filename)[0] + '.png'
        maxH, maxW = imageDimenstion(image_dir + "/" + name)
        
        f = open(json_dir + "/" + filename)
        data = json.load(f)
        for item in data['shapes']: # item is the list
            x, y, height, width = calculateDimension(item['points'])
            writeFile(filename, x/maxW, y/maxH, height/maxH, width/maxW, items[item['label']])
        f.close()
        
        
def calculateDimension(ptsList):
    
    # x, y list
    xList = [ptsList[i][0] for i in range(len(ptsList))]
    yList = [ptsList[j][1] for j in range(len(ptsList))]
    
    xMin = min(xList)
    xMax = max(xList)
    yMin = min(yList)
    yMax = max(yList)
    
    height = yMax - yMin
    width = xMax - xMin
    
    xCenter = (xMax + xMin)/2
    yCenter = (yMax + yMin)/2
    
    return xCenter, yCenter, height, width

def writeFile(filename, x, y, h, w, label):
    name = os.path.splitext(filename)[0] + '.txt'
    data = [label, x, y, w, h]
    with open('data/labeltxt/' + name, "a") as f:
        for i in range(len(data)):
            f.write(str(data[i]))
            if not i == len(data) - 1:
                f.write(' ')
        f.write('\n')

labelme2yolo()