import json
import os
import numpy as np

json_dir = "data"
        
items = {
    'tsuyu' : 0,
    'soySauce' : 1,
    'oil' : 2,
    'mirin' : 3
}

def labelme2yolo():
    json_file_names = [filename for filename in os.listdir(json_dir) if filename.endswith('.json')]
    
    for filename in json_file_names:
        f = open('data/' + filename)
        data = json.load(f)
        for item in data['shapes']: # item is the list
            x, y, height, width = calculateDimension(item['points'])
            writeFile(filename, x, y, height, width, items[item['label']])
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
    data = [label, x, y, h, w]
    with open('data/labeltxt/' + name, "a") as f:
        for val in data:
            f.write(str(val))
            f.write(' ')
        f.write('\n')


labelme2yolo()