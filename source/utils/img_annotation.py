import os
import cv2
import argparse
import pandas as pd


if __name__ == '__main__':

    # Argument parser
    argpars = argparse.ArgumentParser()
    argpars.add_argument("--img-folder", required=True, help="INFO >> Path to the folder containing the images to label.")
    args = argpars.parse_args()

    # Get list of files in the folder
    if not os.path.exists(args.img_folder):
        raise RuntimeError(f"Path {args.img_folder} not exists!")

    file_list = os.listdir(args.img_folder) # conterrà le foto
    file_list.sort()

    # Check if the labels file exists
    if os.path.exists("../../annotations/annotations.csv"):
        print("INFO >> Continuing existing annotation...")
        df = pd.read_csv(f"group_{args.group_id}.csv", index_col=False)

    else:
        print("INFO >> New annotation...")
        data = {
            "file_name": file_list,
            "smoke": [-1]*len(file_list),
        }

        df = pd.DataFrame(data=data)
    
    for row in df.iterrows():
        if row[1][1] == -1:
            try:
                img = cv2.imread(os.path.join(args.img_folder, row[1][0]))
                cv2.imshow("Current frame", img)
                cv2.waitKey(50)

                labels = [-1]

                while labels[0] not in [1, 0]:
                    try:
                        labels[0] = int(
                            input("INFO >> Does the frame has smoke inside? (0 = NO, 1 = YES) "))
                    except ValueError:
                        print("INFO >> Please insert an integer value!")


                df.loc[row[0], ["smoke"]] = labels[0]
                cv2.destroyAllWindows()
                cv2.waitKey(50)

            except KeyboardInterrupt:
                break
    
    df.to_csv("../../annotations/annotations.csv", index=False, header=False)
