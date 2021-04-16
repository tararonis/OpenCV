"""
FU
"""
import cv2 as cv


def rec_face(frame, haar_cascade):
    """
    Get frame and returns list of rectangles with face coordinates
    """
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    return faces_rect


def draw_text(frame, text):
    """
    Draw text in the right bottom corner of the frame
    """
    cv.putText(
        frame,
        text,
        (frame.shape[1] - 110, frame.shape[0] - 20),
        cv.FONT_HERSHEY_TRIPLEX,
        6.0,
        (0, 0, 255),
        7,
    )


def draw_faces(frame, faces):
    """
    Get the frame and list of rectangles with face coordintes
    """
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)


def file(haar_cascade):
    """
    Read the file and recognize faces
    """
    img = cv.imread("Photos/girls.jpg")
    # img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), cv.INTER_LINEAR)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("GRAY person", gray)

    faces_rect = rec_face(gray, haar_cascade)

    # print(f'Number of faces: {len(faces_rect)}')
    draw_text(img, str(len(faces_rect)))

    draw_faces(img, faces_rect)

    cv.imshow("original", img)

    cv.waitKey(0)


def web_cam(haar_cascade):
    """
    Recognize face from the web cam video
    """
    capture = cv.VideoCapture(0)

    while True:        
        isTrue, frame = capture.read()
        faces = rec_face(frame, haar_cascade)
        draw_text(frame, str(len(faces)))
        draw_faces(frame, faces)

        cv.imshow("Video", frame)

        if cv.waitKey(20) & 0xff == ord("d"):
            break


def main():
    """
    Entry point
    """
    haar_cascade = cv.CascadeClassifier("haar_face.xml")
    # file(haar_cascade)
    web_cam(haar_cascade)


if __name__ == "__main__":
    main()
