from flask import Flask, render_template, request
import numpy as np
import io
import torch
import cv2
import matplotlib.pyplot as plt



app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def welcome():
    if request.method=='GET':
        return render_template('index.html')
    
    uploads = request.files['file']
    if uploads.filename != '':
               
        uploads.save(f'static/result.png')
    
    file_location = f'static/result.png'
    preprocess(f"static/result.png")

    return render_template('index.html', file_location=file_location)




def preprocess(img_path):
       
    model = torch.hub.load('ultralytics/yolov5',model='custom', path='./yolov5signs.pt')
    img = cv2.imread(img_path)
    results = model(img)
    for i in results.pred:
        for x, y, w, h, conf, classes in i:
            x=int(x.item())
            y=int(y.item())
            w=int(w.item())
            h=int(h.item())
            classes=int(classes.item())
            cv2.rectangle(img, (x, y), (w, h), (255,0,0), 2)
            cv2.putText(img,f'{results.names[classes]}',(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(3,255,0), 2)
    cv2.imwrite(img_path, img)
    


if __name__ == "__main__":
    app.run(debug=True)
