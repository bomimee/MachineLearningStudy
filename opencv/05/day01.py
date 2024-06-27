#open cv
import  cv2

print('hello open cv', cv2.__version__)

cap = cv2.VideoCapture()
cap.open(0)
if not cap.isOpened():
    print("Camera open failed")
    
print('width:' , round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('height:' , round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()


    #카메라로부터 한 프레임을 받아오면
    #엣지 이미지 내의 중요한 특징을 추출하고 , 물체의 경계를 탐지하는데 매우 유효
