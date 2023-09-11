# Traffic Sign Detection using Transfer Learning on YOLOv5 architecture

Following repository contains the inference code and the flask app for detection of traffic signs using YOLOv5 architecture.

The dataset can be found [here](https://www.kaggle.com/datasets/ahemateja19bec1025/trafficsignlocalizationdetectionyoloannotated), though the annotation for YOLOv5 was done manually for this project and the dataset annotations have not been used.

To create the environment, simply run `pip install -r requirements.txt`, preferably inside a virtual environment.

To launch the Flask app, run `flask --app main.py run` 

Upon detection of the signs, the image will be stored in a `static` folder

