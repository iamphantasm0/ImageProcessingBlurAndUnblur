# Python Program to blur image

# Importing cv2 module
import cv2

# importing os module  
import os



# Image path
image_path = r'C:\blurndeblur\1.jpg'
  
# Image directory
directory = r'C:\blurndeblur\images\savedBlurImg'

# bat.jpg is the batman image.
img = cv2.imread(image_path)

# Change the current directory 
# to specified directory 
os.chdir(directory)

#List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
print("Before saving image:")  
print(os.listdir(directory)) 
  
# Filename
filename = 'blurred.jpg'

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (25,25),0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, gausBlur)
  
# List files and directories  
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'  
print("After saving image:")  
print(os.listdir(directory))
  
print('Successfully saved')
