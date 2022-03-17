import os, sys, cv2, csv, argparse, random
import numpy as np

def init_parameter():   
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument("--data", type=str, default='foo_test.csv', help="Dataset labels")
    parser.add_argument("--images", type=str, default='foo_test/', help="Dataset folder")
    parser.add_argument("--results", type=str, default='foo_results.csv', help="CSV file of the results")
    args = parser.parse_args()
    return args

args = init_parameter()

# Reading CSV test file
with open(args.data, mode='r') as csv_file:
    gt = csv.reader(csv_file, delimiter=',')
    gt_num = 0
    b_dict = {}
    m_dict = {}
    g_dict = {}
    for row in gt:
        b_dict.update({row[0]: int(round(float(row[1])))})
        m_dict.update({row[0]: int(round(float(row[2])))})
        g_dict.update({row[0]: int(round(float(row[3])))})
        gt_num += 1

# Opening CSV results file
with open(args.results, 'w', newline='') as res_file:
    writer = csv.writer(res_file)
    # Processing all the images
    for image in b_dict.keys():
        img = cv2.imread(args.images+image)
        if img.size == 0:
            print("Error")
        # Here you should add your code for applying your DCNN
        b = random.randint(0, 1)
        m = random.randint(0, 1)
        g = random.randint(0, 1)
        # Writing a row in the CSV file
        writer.writerow([image, b, m, g])