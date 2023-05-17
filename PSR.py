import cv2
from skimage.metrics import peak_signal_noise_ratio


def calculate_snr(image_path, reference_path):
    # Load the images
    image = cv2.imread(image_path)
    reference = cv2.imread(reference_path)

    # Calculate the SNR
    snr = peak_signal_noise_ratio(image ,reference)

    # Print the SNR value
    print(f"SNR: {snr} dB")


image_path = "Images/C.jpg"
reference_path = "Images/C_Lesscompressed_Imgupscaler_Resized.jpg"

calculate_snr(image_path, reference_path)
