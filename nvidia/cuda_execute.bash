#!/bin/bash

for i in {0..199}; do  (cd global/ && ./detector_gpu_global.exe) 1>> Error ; done

for i in {0..199}; do  (cd shared/ && ./detector_gpu_shared.exe) 1>> Error ; done

for i in {0..199}; do  (cd texture/ && ./detector_gpu_texture.exe) 1>> Error ; done
