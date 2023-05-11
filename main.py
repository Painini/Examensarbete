import cv2
from skimage.metrics import structural_similarity as ssim

originalImg = cv2.imread('Images/A.png') #Load Unchanged PNG file here
upscaledImg = cv2.imread('Images/AJPGimgupscaler.jpg') #Load Upscaled JPG file here

score, diff = ssim(originalImg, upscaledImg, full=True)

print ("SSIM score: " + score)
