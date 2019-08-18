import rawpy
import imageio
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

output_path = './output'

def main():
    paths = filedialog.askopenfilenames()
    numberOfFiles = len(paths)
    successfullConversions = 0
    print("{0} files selected ...".format(numberOfFiles))

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    fileCounter = 1
    for path in paths:
        print("Processing file {0}/{1}".format(fileCounter, numberOfFiles))

        try:
            with rawpy.imread(path) as raw:
                rgb = raw.postprocess()
                imageio.imsave('output/file{0}.jpg'.format(fileCounter), rgb)
                successfullConversions += 1
        except:
            print('{0} was not processed due to failure ...'.format(path))
        
        fileCounter += 1

    print("Done! {0}/{1} files successfully converted".format(successfullConversions, numberOfFiles))

if __name__ == "__main__":
    main()