"""
Aim:
Create an algorithm that can detect the apriltag
Find the distance between the center of the frame to the apriltag
"""

import time
import matplotlib.pyplot as plt
import numpy as np
from dt_apriltags import Detector
import cv2

cap = cv2.VideoCapture('AprilTagTest.mkv')
success = cap.grab()
frames = []
slopes = []
at_detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.4,
                       debug=0)
cameraMatrix = np.array([ 1060.71, 0, 960, 0, 1060.71, 540, 0, 0, 1]).reshape((3,3))
camera_params = (cameraMatrix[0,0], cameraMatrix[1,1], cameraMatrix[0,2], cameraMatrix[1,2] )
i=0

while success:
    if i % 100  == 0:
        
        _, frame = cap.retrieve()
        height, width, depth = frame.shape
        center = (int(width/2),int(height/2))
        print(center)
        cv2.line(frame, (int(width/2), center[1]-50), (int(width/2), center[1]+50), (255, 0, 0), 5)
        cv2.line(frame, (center[0]-50,int(height/2)), (center[0]+50, int(height/2)), (255, 0, 0), 5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = at_detector.detect(frame, True, camera_params, 0.1)
        color_img = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        for tag in tags:
            for idx in range(len(tag.corners)):
                #drawing the lines and write text
                cv2.line(color_img, tuple(tag.corners[idx - 1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)), (0, 255, 0))
                cv2.putText(color_img, str(tag.tag_id),
                org=(tag.corners[0, 0].astype(int) + 10, tag.corners[0, 1].astype(int) + 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=2,
                color=(0, 0, 255))
            (cX, cY) = (int(tag.center[0]), int(tag.center[1]))
            cv2.circle(color_img, (cX, cY), 5, (0, 0, 255), -1)
            dist = (cX-center[0],cY-center[1])
            print(f"distance: {dist[0],dist[1]}")
            cv2.line(color_img,center,(int(cX),int(cY)),(0, 0, 255),5)

        plt.imshow(color_img)
        plt.pause(0.01)  # Pause for a short time to show the figure
        plt.clf()
    i+=1
    success = cap.grab()
# Release the video capture
cap.release()

# Close the plot window
plt.close()