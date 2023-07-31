import cv2
import numpy as np
import matplotlib.pyplot as plt
from dt_apriltags import Detector

#question 1
def detect_lines(img:str, threshold1:int = 50, threshold2:int = 150, apertureSize:int = 3, minLineLength:int = 100, maxLineGap:int = 10) ->np.ndarray:
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2, apertureSize)  # Detect edges
    lines = cv2.HoughLinesP(
                edges,
                1,
                np.pi/180,
                100,
                minLineLength,
                maxLineGap,
        ) # detect lines
    return lines

# Question 2
def draw_lines(img:str, lines:list, color:tuple = (0, 255, 0)):
    
    for line in lines:
        print(line)
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, f"{x1}, {y1}, {x2}, {y2}", ((x1+x2)/2, (y1+y2)/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    plt.imshow(img)
    

# Question 3
def get_slopes_intercepts(lines: list):
    slopes = []
    intercepts = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2-y1)/(x2-x1)
        slopes.append(slope)
        y_intercept = y2-slope*x2
        x_intercepts = (-1*y_intercept)/slope
        intercepts.append(x_intercepts)
    
    return np.array([slopes, intercepts])

def detect_lanes(lines:list):
    slope, x_intercepts = get_slopes_intercepts(lines)
    print("slope: ", slope)
    print("x: ", x_intercepts)
    



if __name__ == "__main__":
    print(detect_lines("rov_pool.jpg",600,1200,5,500,30))
    print(get_slopes_intercepts(detect_lines("rov_pool.jpg",600,1200,5,500,30)))
