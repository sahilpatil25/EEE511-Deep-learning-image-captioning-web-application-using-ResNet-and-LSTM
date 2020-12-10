# Image Captioning steps

To run the Image captioning application, firstly we need to train our model.

## First step

User needs to clone the repository: https://github.com/sahilpatil25/EEE511-Deep-learning-image-captioning-web-application-using-ResNet-and-LSTM

## Second step:
## Dataset download:
We are using the COCO dataset to train our model. To download the dataset run the commands from the RESTApi/download.sh file.


## Third step:
## Data preprocessing:
To train our model, we do need a large vocabulary to make a captioning task with better accuracy. For this task run the RESTApi/build_vocab.py from the repository. 
Resizing the images:
We are using RESNET model to extract the features from the images. To train the RESNET model, we have to provide the input images with a fixed size of 256 X 256. For this purpose, we have to resize all the input images to 256 X 256 size. To do this task, run the  RESTApi/resize python file from the repository.

## Fourth step:
## Train the model:
We have annotated captions and resized images ready with us. Now train the model on this resized images and annotated captions.
To start the model training run the RESTApi/train.py file from the repository.

## Fifth step:
## Test the model:
To test the model run the below command:
python sample.py --image=”<image file>”

You can put any image and give its path to test the image captioning model.

## To run the web application:
## First step:
To start the REST api, run the RESTApi/main.py file. 
## Second step:
To run the front end app, go to FrontEnd directory and run a python server to serve static application files
Run local python server using the following command - <python -m http.server 9000> (You can also use VS code's live server plugin)
Open Mozilla Firefox (recommended) and go to localhost:9000 to view the application page.
