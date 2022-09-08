from bound_box import bound_box_and_predict
import cv2
from tkinter import *
from PIL import Image, ImageTk

def mask_image(label, imagePath):
	global image
	image = imagePath
	
	# load input image and preprocess
	frame = cv2.imread(imagePath)

	bound_box_and_predict(frame)

	# show output image
	#cv2.imshow("Output", frame)
	frame =cv2.resize(frame, dsize=(450, 300), fx=0.5, fy=0.5)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(cv2image)

    # Convert image to PhotoImage
	label.configure(image = None)
	imgtk = ImageTk.PhotoImage(image = img)
	label.imgtk = imgtk
	label.configure(image = imgtk)
	#cv2.waitKey(0)
	cv2.destroyAllWindows()
