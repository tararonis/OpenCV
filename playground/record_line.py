"""
Saw some videos with an interesting filter.
There is a line traveling from left border to right ahd the part of image behind the line freezes.
That as result creates a 'funny' image.
1. Grab video from webcam.
2. Create a line that passing throw the image.
3. Crop part of the video passed by line with 1 step.
4. Create a blank frame and simultiniously update it every tick.
5. Add to blank frame the remainig part of the original frame.
    5.1 Make it dimmer
6. ...
7. Profit
"""
import cv2 as cv
import numpy as np


def main():
    """
    Entry point
    """
    # Init the camera
    capture = cv.VideoCapture(0)

    # Tricky thing-if camera is busy opencv raising the warning instead of exception
    if capture.isOpened():
        # get the width and height of the video source and create a blank frame
        width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

        blank = np.zeros((height, width, 3), dtype="uint8")

        # Every tick line will go forward 5 pixels
        step = 5
        x_start = 0
        x_next = x_start + step

        while True:
            _, frame = capture.read()

            # create walking line
            pt1 = (int(x_next + 3), 0)
            pt2 = (int(x_next + 3), frame.shape[0])

            cv.line(frame, pt1, pt2, (0, 0, 255), 6)

            # add passed part of the original frame
            blank[0 : frame.shape[0], x_start:x_next] = frame[
                0 : frame.shape[0], x_start:x_next
            ]

            # to reduce the brighnest:
            # convert to hsv format
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            # and reduce the value
            frame[::2] = frame[::2] * 0.3

            # then convert back to bgr
            frame = cv.cvtColor(frame, cv.COLOR_HSV2BGR)

            # added the other part of the frame
            blank[0 : frame.shape[0], x_next : frame.shape[1]] = frame[
                0 : frame.shape[0], x_next : frame.shape[1]
            ]

            # increase the coordinates
            if x_next + step < frame.shape[1]:
                x_start, x_next = x_next, x_next + step
            else:
                x_start, x_next = (
                    0,
                    step,
                )  # run "record line" in loop-start again after it reach the right border

            cv.imshow("Video", frame)
            cv.imshow("Mem", blank)

            if cv.waitKey(20) & 0xff == ord("d"):
                break

        capture.release()
        cv.destroyAllWindows()
    else:
        print("Can't get access to camera")


if __name__ == "__main__":
    main()
