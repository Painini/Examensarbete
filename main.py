import cv2
from skimage.metrics import structural_similarity as ssim

originalImg = cv2.imread("Original Image here") #Load Unchanged PNG file here
upscaledImg = cv2.imread("Upscaled Image here") #Load Upscaled JPG file here

score, diff = ssim(originalImg, upscaledImg, full=True)

print ("SSIM score: " + score)
