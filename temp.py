import tkinter as tk
from PIL import ImageGrab
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'


class SketchPad:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.is_drawing = False
        self.previous_x = None
        self.previous_y = None

        self.convert_button = tk.Button(self.root, text="Convert to Text", command=self.convert_to_text)
        self.convert_button.pack()

    def start_drawing(self, event):
        self.is_drawing = True
        self.previous_x = event.x
        self.previous_y = event.y

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            self.canvas.create_line(self.previous_x, self.previous_y, x, y, fill="black", width=3)
            self.previous_x = x
            self.previous_y = y

    def stop_drawing(self, event):
        self.is_drawing = False

    def convert_to_text(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        image = ImageGrab.grab(bbox=(x, y, x1, y1))
        text = pytesseract.image_to_string(image)

        if text:
            print("Converted Text:")
            print(text)
        else:
            print("No text detected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sketch Pad")
    sketch_pad = SketchPad(root)
    root.mainloop()
