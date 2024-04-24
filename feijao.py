import cv2
import numpy as np

imagem = cv2.imread('contarfeijoes/feijoes.png')

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lower_black = np.array([0, 0, 12])
upper_black = np.array([180, 255, 46])
lower_brown = np.array([10, 50, 50])
upper_brown = np.array([30, 255, 255])

mask_black = cv2.inRange(hsv, lower_black, upper_black)
mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)

contornos_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_brown, _ = cv2.findContours(mask_brown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contador_feijao_preto = 0
contador_feijao_carioca = 0

for contorno in contornos_black:
    area = cv2.contourArea(contorno)
    if area > 100:
        contador_feijao_preto += 1

for contorno in contornos_brown:
    area = cv2.contourArea(contorno)
    if area > 100:
        contador_feijao_carioca += 1

print("Número de feijões pretos:", contador_feijao_preto)
print("Número de feijões cariocas:", contador_feijao_carioca)

cv2.drawContours(imagem, contornos_black, -1, (0, 255, 0), 2)
cv2.drawContours(imagem, contornos_brown, -1, (0, 0, 255), 2)

cv2.imshow('Contornos', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()