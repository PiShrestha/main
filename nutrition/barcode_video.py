from imutils.video import VideoStream
from pyzbar import pyzbar
import cv2

def getBarcode():
    # starts video stream
    vs = VideoStream(src=0).start()
    found = set()

    while True:
        # every frame is broken down/resized
        frame = vs.read()
        # decode frame to have list of frames
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            found.add(barcodeData)
        # shows camera window to user and waits for key
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
        # 'q' closes the window or when a barcode is found
        if key == ord('q') or len(found) > 0:
            break

    # closes all windows, and ends video stream
    cv2.destroyAllWindows()
    vs.stop()
    
    return list(found)
