import tkinter as tk
import subprocess
import sys
from tkinter import messagebox
from ultralytics import YOLO
import cv2
from tkinterdnd2 import TkinterDnD
from PIL import Image, ImageTk
from tkinter import filedialog

model = YOLO("yolov8n.pt")

from tkinterdnd2 import TkinterDnD
from PIL import Image, ImageTk
import os

def drop(event):
    file_path = event.data
    # Remove the curly braces
    file_path = file_path.strip('{}')
    # Check if the file is an image or a video
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        root.file_type = 'image'
        img = Image.open(file_path)
        img = img.resize((800, 600), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        frame1.panel = tk.Label(frame1, image=img)
        frame1.panel.image = img
        frame1.panel.pack()
    else:
        root.file_type = 'video'
        cap = cv2.VideoCapture(file_path)
        def show_frame():
            ret, frame = cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                img = img.resize((800, 600), Image.LANCZOS)
                imgtk = ImageTk.PhotoImage(image=img)
                if hasattr(frame1, 'panel'):
                    frame1.panel.imgtk = imgtk
                    frame1.panel.config(image=imgtk)
                else:
                    frame1.panel = tk.Label(frame1, image=imgtk)
                    frame1.panel.imgtk = imgtk
                    frame1.panel.pack()
                frame1.after(10, show_frame)
            else:
                cap.release()
        show_frame()
    # Save the file path
    root.image_path = file_path



def train():
    if root.file_type == 'image':
        model.predict(source=root.image_path, show=True, conf=0.5)
    else:
        model.predict(source=root.image_path, show=True, conf=0.5)

def exit_app():
    messagebox.showinfo("Thoát", "Bạn chắc chắn muốn thoát không??")
    root.quit()

def clear_image():
    if hasattr(frame1, 'panel'):
        frame1.panel.pack_forget()
        del frame1.panel

def start():
    subprocess.Popen(['python', 'index1.py'])
    sys.exit()
root = TkinterDnD.Tk()
root.geometry('800x600')
# Use a different relief style for the frames
frame1 = tk.Frame(root, width=560, height=600, bd=8, relief='sunken')
frame1.pack_propagate(0)
frame1.pack(side=tk.LEFT)
frame1.drop_target_register('DND_Files')
frame1.dnd_bind('<<Drop>>', drop)

frame2 = tk.Frame(root, width=240, height=600, bd=8, relief='sunken')
frame2.pack(side=tk.RIGHT)

# Change the color and font of the buttons
button1 = tk.Button(frame2, text="Mở Camera", command=start, height=2, width=30, fg='black', font=('Helvetica', '16'))
button1.pack(pady=20)

button2 = tk.Button(frame2, text="Nhận Biết Ảnh", command=train, height=2, width=30, fg='black', font=('Helvetica', '16'))
button2.pack(pady=20)

button3 = tk.Button(frame2, text="Xóa Ảnh", command=clear_image, height=2, width=30,  fg='black', font=('Helvetica', '16'))
button3.pack(pady=20)

root.mainloop()
