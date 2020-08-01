### Contents
  1.  Presentation
  2. Inference Images.
  3. Jupyter Notebook
  4. Additional Files
  
### Road Damage Dataset 
Road Damage Dataset contains trained models and Annotated images.
Annotated images are presented as the same format to [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/).

WE HAVE USED FASTER R-CNN INCEPTION V2 MODEL to train the images
Structures of folders here is:

        TensorFlow
        |─ addons
        │   └─ labelImg
        ├─ models
        │   ├─ official
        │   ├─ research
        │   ├─ samples
        │   └─ tutorials
        └─ workspace
            └─ training_demo


            training_demo
            ├─ annotations
            ├─ images
            │   ├─ test
            │   └─ train
            ├─ pre-trained-model
            ├─ training
            └─ README.md


### **Here’s an explanation for each of the folders/filer shown in the above tree:**

**annotations:** This folder will be used to store all *.csv files and the respective TensorFlow *.record files, which contain the list of annotations for our dataset images.

**images:** This folder contains a copy of all the images in our dataset, as well as the respective *.xml files produced for each one, once labelImg is used to annotate objects.

**images\train:** This folder contains a copy of all images, and the respective *.xml files, which will be used to train our model.
images\test: This folder contains a copy of all images, and the respective *.xml files, which will be used to test our model.
pre-trained-model: This folder will contain the pre-trained model of our choice, which shall be used as a starting checkpoint for our training job.

**training:** This folder will contain the training pipeline configuration file *.config, as well as a *.pbtxt label map file and all files generated during the training of our model.

**README.md:** This is an optional file which provides some general information regarding the training conditions of our model. It is not used by TensorFlow in any way, but it generally helps when you have a few training folders and/or you are revisiting a trained model after some time.


## **Steps to complete the similar process: (may vary depending on your machine):**

1. Set up the above heirarchy,  preferably in C:\Users\<YOUR NAME>\
2. After we have our annotations and split our dataset into the desired training and testing subsets, it is time to convert our annotations into the so called TFRecord format. <br/>
    There are two steps in doing so: <br/><br/>
    1. Converting the individual *.xml files to a unified *.csv file for each dataset. <br/>
    2. Converting the *.csv files of each dataset to *.record files (TFRecord format). <br/><br/>
3. Using xml_to_csv.py we can do the step 2 <br/>
4. Using generate_tfrecord.py we can finally then create TFRecord for both training and testing. <br/>
5. Download the faster_rcnn_inception_v2 model from tensorflow zoo repo. Extract in pre-trained-models. <br/>
6. Make Corresponding changes in config file took from samples in models/research/object_detection/samples/config/* <br/><br/>
    1. Edit number of class to required classes
    2. Select suitable batch size (more -> more memory)
    3. Set all the paths needed there<br/><br/>
7. Before we begin training our model, let’s go and copy the TensorFlow/models/research/object_detection/legacy/train.py script and paste it straight into our training_demo folder. We will need this script in order to train our model. Now, to initiate a new training job, cd inside the training_demo folder and type the following: <br/><br/>
    python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/<your_config_file>.config  <br/><br/><br/>
8. Wait till the model trains the go export it then finally test it.
9. Copy the TensorFlow/models/research/object_detection/export_inference_graph.py script and paste it straight into your training_demo folder. Check inside your training_demo/training folder for the model.ckpt-* checkpoint file with the highest number following the name of the dash e.g. model.ckpt-250). This number represents the training step index at which the file was created. Alternatively, simply sort all the files inside training_demo/training by descending time and pick the model.ckpt-* file that comes first in the list. Make a note of the file’s name, as it will be passed as an argument when we call the export_inference_graph.py script. <br/>
Now, cd inside your training_demo folder, and run the following command: <br/><br/>
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/<your_config_file>.config --trained_checkpoint_prefix training/model.ckpt-250 --output_directory trained-inference-graphs/output_inference_graph_v1.pb <br/><br/>
 

