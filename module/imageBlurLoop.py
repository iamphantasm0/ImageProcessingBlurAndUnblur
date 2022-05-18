import os
# Importing cv2 module
import cv2

def blurImageWithLoop():
    # Image Save directory
    saveDirectory = r'C:\ImageProcessingBlurAndUnblur\images\savedBlurImg'

    saveDirectory = r'C:\ImageProcessingBlurAndUnblur\images\savedBlurImg'

    # Imge directory
    directory = r'C:\ImageProcessingBlurAndUnblur\images\imgF'

    list_of_img = os.listdir(directory)

    #file name
    filenamePre = 1
    filenamePost = '.jpg'

    for image in list_of_img:
        img = cv2.imread(os.path.join(directory, image))
        # print(img)
        # cv2.imshow('image', img)
        # cv2.imwrite('img1.jpg',img)
        gausBlur = cv2.GaussianBlur(img, (25,25),0) 
        # cv2.imshow('Gaussian Blurring', gausBlur)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        os.chdir(saveDirectory)
        print("Before saving image:")  
        filename = str(filenamePre) + filenamePost
        print(filename)
        filenamePre += 1
        cv2.imwrite(filename, gausBlur)
        print("After saving image:")  
        print(os.listdir(directory))
        print('Successfully saved')


