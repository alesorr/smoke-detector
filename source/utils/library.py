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
        self.images = []

    def load_from_dir(self, dataset_type="train/"):
        """
        This method loads all the train/test images from dataset folders
        """
        print("Loading images...")
        for dataset in os.listdir(self.image_path + dataset_type):
            for idx in os.listdir(self.image_path + dataset_type + dataset + "/"):
                #images_folder = "" if (idx == ".DS_Store") else self.image_path + dataset_type + dataset + "/" + idx
                images_folder = self.image_path + dataset_type + dataset + "/" + idx
                images_count = 0 if images_folder is None else len(os.listdir(images_folder))
                #print("INFO >> Loading images from " + images_folder)
                for _ in range (images_count):
                    for image in os.listdir(images_folder):
                        # check if the image ends with jpg
                        if (image.endswith(".jpg")):
                            self.images.append(image)

        print("INFO >> " + str(len(self.images)) + " images loaded.")
        return len(self.images)
        