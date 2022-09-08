# import the necessary packages
from imutils.video import VideoStream
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
from bound_box import bound_box_and_predict

# def show_frame():
#     # Convert image to PhotoImage
#     label.configure(image = None)
#     imgtk = ImageTk.PhotoImage(image = img)
#     label.imgtk = imgtk
#     label.configure(image = imgtk)
#     label.after(2, show_frame)

def mask_video(videoPath):
	# initialize the video stream
	print("[INFO] starting video stream...")
	# global vs, label
	# label = labelRight
	vs = VideoStream(src=videoPath).start()
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=600)

		bound_box_and_predict(frame)
		# show the output frame
		cv2.imshow("Output", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q") or key == 13:
			break

	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()