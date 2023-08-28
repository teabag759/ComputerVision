import cv2 as cv
import sys

img=cv.imread('../sourceImage/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

BrushSiz = 5    # 붓의 크기
LColor, RColor = (255, 0, 0), (0, 0, 255)   # 파란색과 빨간색

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)    # 마우스 왼쪽 -> 파란색
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)    # 마우스 왼쪽 -> 빨간색
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)    # 마우스 왼쪽 클릭하며 이동 -> 파란색
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)    # 마우스 오른쪽 클릭하며 이동 -> 빨간색

    cv.imshow('Painting', img)  # 수정된 영상을 다시 그림

cv.namedWindow('Painting')
cv.imshow('Painting', img)

cv.setMouseCallback('Painting', painting)

while(True):                        # 마우스 이벤트가 언제 발생할 지 모르므로 무한 반복
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


