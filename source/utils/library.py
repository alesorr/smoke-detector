#!/usr/bin/env python3

import sys
import os
from os import listdir

sys.path.insert(1, '/Users/alex/Desktop/smoke-detector/source/utils/')
import config

'''
Class which contains all the methods that concerns with the detector built
'''
class Detector:
    
    def __init__(self):
        self.model = config.MODEL_PATH


class ImageLoader:

    def __init__(self):
        self.image_path = config.DATASET_PATH

    def load_from_dir(self, dataset_type="train/"):
        """
        This method loads all the train/test images from dataset folders
        """
        try:
            for dataset in os.listdir(self.image_path + dataset_type):
                for idx in os.listdir(self.image_path + dataset_type + dataset + "/"):
                    images_folder = None if (idx == ".DS_Store") else self.image_path + dataset_type + dataset + "/" + idx
                    images_count = 0 if images_folder is None else len(os.listdir(images_folder))
                    print("INFO >> Loading images from " + images_folder)
                    for _ in range (images_count):
                        for images in os.listdir(images_folder):
                            # check if the image ends with jpg
                            if (images.endswith(".jpg") and images != ".DS_Store"):
                                print(images)

        except:
            pass
        