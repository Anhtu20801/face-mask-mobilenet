from detect_mask_image import mask_image
from detect_mask_webcam import mask_video

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd


def handleImageButton():
    filename = fd.askopenfilename(
        filetypes=(
            ('image files', '*.jpg'),
            ('All files', '*.*')
        )
    )
    mask_image(labelRight, filename)


def handleVideoButton():
    filename = fd.askopenfilename()
    mask_video(filename)

def handleMaskWebCamButton():
    mask_video(0)
    

if __name__ == '__main__':

    background = '#5ba4fc'
    bgButton = '#f8f8f8'
    activeBgBtn = '#e6e6e6'
    colorButton = '#000000'

    #Create window
    window = tk.Tk()
    window.title('Nhóm 13')

    window_width = 820
    window_height = 400
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.configure(bg = background)

    #Left frame
    left_frame = Frame(window, bg = background,
                        padx = 20, pady = 5
                )
    left_frame.pack(side = tk.LEFT)
    #Right frame
    global right_frame
    right_frame = Frame(window, bg = '#f8f8f8',
                        padx = 5, pady= 5
                )
    right_frame.pack(side =tk.RIGHT)
    #Label
    labelLeft = Label(left_frame, text = 'Chọn chức năng: ',
                    justify= CENTER, 
                    font = ("Times New Roman", 20, 'bold'),
                    fg = 'white', bg = background,
                    pady = 25
                    )
    labelLeft.grid(column = 0, row = 0)

    global labelRight
    labelRight = Label(right_frame, width= '550', height= '300')
    labelRight.grid(column = 0, row = 0, columnspan = 3, rowspan= 3)
    
    #Detect mask image button 
    btnMaskImg = Button(left_frame, text = "Nhận diện qua ảnh", 
                    command = handleImageButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn,
                    cursor = 'mouse'
                )
    btnMaskImg.grid(column = 0, row = 1)
    
    #Detect mask video button 
    btnMaskVideo = Button(left_frame, text = "Nhận diện qua video", 
                    command = handleVideoButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn,
                    cursor = 'mouse'
                )
    btnMaskVideo.grid(column = 0, row = 3)
    
    #Detect mask webcam button 
    btnMaskWebcam = Button(left_frame, text = "Nhận diện qua webcam", 
                    command = handleMaskWebCamButton,
                    font = ("Times New Roman", 12, 'bold'),
                    height = 2, width = 25,
                    bg = bgButton, fg = colorButton,
                    activebackground = activeBgBtn,
                    cursor = 'mouse'
                )
    btnMaskWebcam.grid(column = 0, row = 5)
    
    #Label no text
    Label(left_frame, height = 2, bg = background).grid(column = 0, row = 2)
    Label(left_frame, height = 2, bg = background).grid(column = 0, row = 4)    
    window.mainloop()
