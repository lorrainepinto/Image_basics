
import cv2
import imutils

img = cv2.imread("red.JPG",1)
imge =cv2.resize(img,(600,612))
cv2.imshow("lol",imge)
cv2.waitKey(0)
#
# #cv2.imwrite("pkd.png",img)
#
# corner = imge[0:100, 0:100]
# mid= imge[150:300,250:500]
# cv2.imshow("Corner", corner)
# cv2.waitKey(0)
#
# imge[0:100, 0:100] = (0, 255, 255)
# imge[150:300,250:500] =(255,0,255)
# cv2.imshow("Updated", imge)
# cv2.waitKey(0)
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


