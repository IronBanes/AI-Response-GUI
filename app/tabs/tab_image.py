import os
from PIL import Image
import pandas as pd
import math

import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import customtkinter as ctk
from tkinter import filedialog

class TabImageFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)
        
        self.path = []
        
        #label
        self.folderLabel = ttk.Label(self, text="Select folder to gather images from:") 
        self.folderbutton = ctk.CTkButton(self, text="Select Folder", corner_radius=100, fg_color="#120E2B", command=self.selectFolder)
        #button to start
        self.startbutton = ctk.CTkButton(self, text="Start", corner_radius=100, fg_color="#120E2B")
        #label showing current file
        
        #progressbar
            #current file/total files * 100 = percentage
            #each file will increase progressbar percentage
        
        self.folderLabel.grid(column=0, row=0, sticky="nw",rowspan=1, padx=15, pady=5)
        self.folderbutton.grid(column=0, row=0, sticky="new", padx=15, pady=25)
        self.startbutton.grid(column=0, row=1, sticky="new", padx=15, pady=5)
        
        # self.label.grid(column=0, row=1, sticky="wn",rowspan=1,padx=15,pady=5)
        # self.textbox.grid(column=0, row=1,sticky=" news", padx=15,pady=25)
        
    def selectFolder(self):
        self.path = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), 
                                                              ("png files", "*.png"), 
                                                              ("all files", "*.*")))
        # Access the currentPath attribute through the instance of the self.column1_frame class
        # self.currentPath.set(filename)  # Update the currentPath attribute with the selected directory
    
    def start(self):
        image_data = {}
        for file in self.path:
            img = Image.open(file)
            dpi = img.info['dpi'] if 'dpi' in img.info else (72, 72)
            dpi = (float(dpi[0]) + float(dpi[1])) / 2
            width, height = img.size
            width_in = self.round_half(math.ceil((width / dpi) * 10) / 10)
            height_in = self.round_half(math.ceil((height / dpi) * 10) / 10)
            base_name = os.path.basename(file).rsplit('-', 1)[0]
            if base_name in image_data:
                image_data[base_name]['count'] += 1
                if height_in > image_data[base_name]['height']:
                    image_data[base_name]['width'] = width_in
                    image_data[base_name]['height'] = height_in
            else:
                image_data[base_name] = {'count': 1, 'width': width_in, 'height': height_in}
        df = pd.DataFrame.from_dict(image_data, orient='index')
        df['description'] = df.apply(lambda row: f'Digital reproduction of a {row["width"]}" x {row["height"]}" {int(row["count"])}-page document.', axis=1)
        df.to_excel('output.xlsx', columns=['description'], header=['Format'])
        
    def round_half(self, number):
        return round(number * 2) / 2