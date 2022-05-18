import os
# Importing cv2 module
import cv2
#Importing numpy
import numpy as np

def unblurImageWithLoop():
    # Image Save directory
    saveDirectory = r'C:\ImageProcessingBlurAndUnblur\images\savedUnblurImg'

    saveDirectory = r'C:\ImageProcessingBlurAndUnblur\images\savedUnblurImg'


    # Imge directory
    directory = r'C:\ImageProcessingBlurAndUnblur\images\savedBlurImg'

    list_of_img = os.listdir(directory)

    #file name
    filenamePre = 1
    filenamePost = '.jpg'

    for image in list_of_img:
        image = cv2.imread(os.path.join(directory, image))
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(image, -25, sharpen_kernel)
        os.chdir(saveDirectory)
        print("Before saving image:")  
        filename = str(filenamePre) + filenamePost
        print(filename)
        filenamePre += 1
        cv2.imwrite(filename, sharpen)
        cv2.waitKey()
        print("After saving image:")  
        print(os.listdir(directory))
        print('Successfully saved')


