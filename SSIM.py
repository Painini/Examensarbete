import cv2
from skimage.metrics import structural_similarity as ssim

originalImg = cv2.imread('Images/C.jpg') #Load Unchanged PNG file here
# Load Upscaled JPG file here
upscaledImg = cv2.imread('Images/C_Lesscompressed_Imgupscaler_Resized.jpg')

score = ssim(originalImg, upscaledImg, channel_axis= -1)

print ("SSIM score: " + str(score))
