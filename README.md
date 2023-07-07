# pantry_pal
Please download the weights at the following link:
https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5x6.pt
Place it in the yolo5 folder

Training command
python .\yolov5\train.py --img 640 --cfg .\yolov5\models\yolov5x.yaml --hyp .\yolov5
\data\hyps\hyp.scratch-high.yaml --batch 32 --epochs 100 --data .\data\YOLODataset\dataset.yaml --weights .\yolov5\yolov5x6.pt --workers 24 --name yolo_pantry_pal
<<<<<<< HEAD

Test command
python yolov5\detect.py --weights data\trainedWeights\best.pt --source data\YOLODataset\images\val\1.png
=======
>>>>>>> 5892f1c2b369aef538ced81f19f4f541ef13de53
