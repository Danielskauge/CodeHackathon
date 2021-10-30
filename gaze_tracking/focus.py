from __future__ import annotations
import cv2
from gaze_tracking import GazeTracking

camera=cv2.VideoCapture(0)
gaze=GazeTracking()
blinks=0
attention=True
while(True):

    _,face=camera.read()
    face=cv2.flip(face,1)
    gaze.refresh(face)
    face=gaze.annotated_frame()
    cv2.putText(face, "Blinks: "+str(blinks),(90,130),cv2.FONT_HERSHEY_COMPLEX,1,(147,58,31),1)
    if(gaze.is_blinking()):
        blinks+=1
    if(not gaze.is_center()):
        cv2.putText(face, "Attention: False", (90,60),cv2.FONT_HERSHEY_COMPLEX, 0.9,(147,58,31),1)
    else:
         cv2.putText(face, "Attention: True", (90,60),cv2.FONT_HERSHEY_COMPLEX, 0.9,(147,58,31),1)
    cv2.imshow("Camera",face)
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

