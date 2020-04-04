import numpy as np
import cv2

# Empty point coordinate lists
pts = []


# Computing and executing transformation
def rectify():
    global pts
    if (len(pts) % 4 == 0):
        # Destination points
        pts2 = [(0,0),(0, 255),(255,255),(255,0)] # order: (left-bottom, left-top, right-top, right-bottom)
        num = len(pts) - 4
        src_pts = np.float32(pts[num:]).reshape(-1, 1, 2)
        dst_pts = np.float32(pts2).reshape(-1, 1, 2)
        M = cv2.getPerspectiveTransform(src_pts, dst_pts)
        if M is None:
            print('No solution found!')
        else:
            image_reg = cv2.warpPerspective(clone, M, (256, 256))
            cv2.imshow('Dice', image_reg)


def click(event, x, y, flags, param):
    global pts, image

    if event == cv2.EVENT_LBUTTONUP:
        # adding (x, y) coordinates to the list
        pts.append((x, y))
        print(pts)

        # Drawing a marker
        cv2.drawMarker(image, (x, y), (0, 255, 0), 3)
        # cv2.circle(image1, (x-1, y-1), 3, (0, 255, 0), 2)
        cv2.imshow('image', image)
        rectify()


image = cv2.imread('dice.png', cv2.IMREAD_GRAYSCALE)
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', click)

# Loop
while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(0) & 0xFF

    if key == ord("r"):
        pts = []
        print(pts)
        image = clone.copy()

    elif key == ord("q"):
        break

# close all open windows
cv2.destroyAllWindows()
