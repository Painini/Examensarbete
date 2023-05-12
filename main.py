import cv2
from skimage.metrics import structural_similarity as ssim

originalImg = cv2.imread('Images/A.jpg') #Load Unchanged PNG file here
upscaledImg = cv2.imread('Images/ACompressedImgupscalerResized.jpg') #Load Upscaled JPG file here

score = ssim(originalImg, upscaledImg, channel_axis= -1)

print ("SSIM score: " + str(score))
