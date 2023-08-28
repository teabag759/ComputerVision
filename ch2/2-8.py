import cv2 as cv
import sys

img = cv.imread('../sourceImage/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:   # 마우스 왼쪽 버튼 선택 시 초기 위치 저장
        ix, iy = x, y
    elif event == cv.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 선택 시 초기 위치 저장
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)

    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):                        # 마우스 이벤트가 언제 발생할 지 모르므로 무한 반복
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break