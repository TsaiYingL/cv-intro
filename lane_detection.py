import cv2
import numpy as np
import matplotlib.pyplot as plt
from dt_apriltags import Detector

#question 1
def detect_lines(img:str, threshold1:int = 50, threshold2:int = 150, apertureSize:int = 3, minLineLength:int = 100, maxLineGap:int = 10):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grayscale
    edges = cv2.Canny(gray,threshold1,threshold2, apertureSize=apertureSize) # detect edges
    lines = cv2.HoughLinesP(
                    edges,
                    1,
                    np.pi/180,
                    100,
                    minLineLength=minLineLength,
                    maxLineGap=maxLineGap,
            ) # detect lines
    return lines

# Question 2
def draw_lines(img:str, lines:list, color:tuple = (0, 255, 0)):
    image = cv2.imread(img)
    
    for line in lines:
        print(line)
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), color, 2)
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    pass

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
