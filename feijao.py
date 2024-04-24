import cv2
import numpy as np

# Load the image
imagem = cv2.imread('feijoes.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Define the color ranges for black and brown beans
lower_black = np.array([0, 0, 12])
upper_black = np.array([180, 255, 46])
lower_brown = np.array([10, 50, 50])
upper_brown = np.array([30, 255, 255])

# Create masks for black and brown beans
mask_black = cv2.inRange(hsv, lower_black, upper_black)
mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)

# Find contours in the binary images
contornos_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_brown, _ = cv2.findContours(mask_brown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize counters for black and brown beans
contador_feijao_preto = 0
contador_feijao_carioca = 0

# Iterate through detected contours
for contorno in contornos_black:
    area = cv2.contourArea(contorno)
    if area > 100:
        contador_feijao_preto += 1

for contorno in contornos_brown:
    area = cv2.contourArea(contorno)
    if area > 100:
        contador_feijao_carioca += 1

# Print the counts of black and brown beans
print("Número de feijões pretos:", contador_feijao_preto)
print("Número de feijões cariocas:", contador_feijao_carioca)

# Draw contours on the original image for visualization
cv2.drawContours(imagem, contornos_black, -1, (0, 255, 0), 2)
cv2.drawContours(imagem, contornos_brown, -1, (0, 0, 255), 2)

# Display the image with drawn contours
cv2.imshow('Contornos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()