import os
import json
import ctypes
import platform

import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import customtkinter as ctk


from tabs.tab_generate import TabGenerateFrame
from tabs.tab_image import TabImageFrame

class App(ttk.Window):
    def __init__(self, title, size):
        super().__init__(themename="darkly")
        
        if platform.system() == "Windows":
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
        
        self.title(title)
        
        
        window_width = size[0]
        window_height = size[1]
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        
        # Limit the window size to be at most 80% of the screen width and height
        window_width = min(window_width, int(0.8 * display_width))
        window_height = min(window_height, int(0.8 * display_height))
        
        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)
        
        self.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.minsize(size[0],size[1])
        self.resizable(True, True)
        
        self.tabControl = ttk.Notebook(self)
        self.tab1 = TabGenerateFrame(self.tabControl)
        self.tab2 = TabImageFrame(self.tabControl)
        self.tabControl.add(self.tab1, text="Generate")
        self.tabControl.add(self.tab2, text="Image")
        self.tabControl.pack(expand=1, fill="both")
        
        self.mainloop()
    
    def setwidth(self, width):
        self.width = width
    
    def setheight(self, height):
        self.height = height

App("AI Generator", (500, 500))