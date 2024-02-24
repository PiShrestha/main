from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2


# same process, setting up argument parser to determine where the data is stored
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv", help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())


# starts video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)


# csv is file that is being written to
csv = open(args["output"], "w")
# set object keeps track of all barcodes detected
found = set()


while True:
    # every frame is broken down/resized
    frame = vs.read()
    frame = imutils.resize(frame, width=1000)


    # same process as other program, this time it is run with each frame, not one still image
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        # form border of barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
       
        # turn the bits into string
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type


        # shows the barcode info in the video stream
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


        # writes unique barcodes to csv file and adds them to found set
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
            csv.flush()
            found.add(barcodeData)


    # shows camera window to user and waits for key
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF


    # 'q' closes the window
    if key == ord('q'):
        break


# closes csv file, closes all windows, and ends video stream
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()