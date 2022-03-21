
import cv2
src = cv2.imread("standardprostate.jpg")
src_gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
src_eqlzd = cv2.equalizeHist(src_gray)

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.imshow('src',src)

cv2.namedWindow('src_gray', cv2.WINDOW_NORMAL)
cv2.imshow('src_gray',src_gray)
cv2.imwrite('spgray.jpg',src_gray)

cv2.namedWindow('src_eqlzd', cv2.WINDOW_NORMAL)
cv2.imshow('src_eqlzd',src_eqlzd)
cv2.imwrite('speqlzd.jpg',src_eqlzd)

cv2.waitKey(0)
cv2.destroyAllWindows()
