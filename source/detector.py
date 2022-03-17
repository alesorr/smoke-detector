#!/usr/bin/env python3

import os
import sys
sys.path.insert(1, '/Users/alex/Desktop/smoke-detector/source/utils/')
import config
import library
  

'''

 See source -> https://github.com/aiformankind/wildfire-smoke-detection-camera/blob/master/object_detection_wildfire.ipynb

'''

def main(text="INFO >> Start..."):
    #print(text)
    return text

if __name__ == "__main__":
    main()
    config.print_all()

    img_loader = library.ImageLoader()
    print("INFO >> Init software...")
    img_loader.load_from_dir()
    