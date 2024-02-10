import tkinter as tk
from tkinter import *

import ttkbootstrap as ttk
import customtkinter as ctk
import os 
import sys 

absolute_path = os.path.dirname(__file__)
relative_path = "modules"
full_path = os.path.join(absolute_path, relative_path)

print(absolute_path)
print(relative_path)
print(full_path)
sys.path.insert(0, full_path)

from aigen import AiGenerate

class TabGenerateFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.aigen_instance = AiGenerate()
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure((1,3), weight=2)
        
        self.string_to_number_mapping = {
            self.aigen_instance.get_instructions_from_file(1): 1,
            self.aigen_instance.get_instructions_from_file(2): 2,
            self.aigen_instance.get_instructions_from_file(3): 3
        }
        self.selected_numerical_value = tk.IntVar()
        
        '''string_gptversion["gpt"] = {
            "gpt-3.5-turbo",
            "gpt-4-turbo-preview"
        }'''
        # self.selected_numerical_value_gpt = tk.IntVar()
        

        self.instructions_label = ttk.Label(self, text="Instructions: Use the dropdown to select the instructions you want to use.")
        
        self.instructions_combobox = ttk.Combobox(
            self, 
            values=list(self.string_to_number_mapping.keys()), 
            textvariable=self.selected_numerical_value
        )
        self.gptversion = tk.StringVar()
        self.gptversion_combobox = ttk.Combobox(
            self,  
            textvariable=self.gptversion
        )
        self.gptversion_combobox['values'] = ("gpt-3.5-turbo", "gpt-4-turbo-preview")
        
        default_option = list(self.string_to_number_mapping.keys())[0]
        default_option_gpt = self.gptversion_combobox['values'][0]
        
        self.instructions_combobox.set(default_option)
        self.label = ttk.Label(self, text="Enter the text to generate:")
        self.textbox = tk.Text(self, height=5, wrap="word", background="#ffffff", relief="flat")
        
        self.gptversion_label = ttk.Label(self, text="GPT Version: Use the dropdown to select the GPT version you want to use.")
        self.gptversion_combobox.set(default_option_gpt)
        self.genbutton = ctk.CTkButton(self, text="Generate", command=self.generate, corner_radius=100, fg_color="#120E2B")        
        #self.genbutton = ttk.Button(self, text="Generate", command=self.generate)
        self.generationout_label = ttk.Label(self, text="Response:")
        self.generation_textbox = tk.Text(self, height=5, wrap="word", background="#ffffff", relief="flat")

        self.instructions_label.grid(column=0, row=0, sticky="new", padx=15, pady=5)
        self.instructions_combobox.grid(column=0, row=0, sticky="sew", padx=15, pady=5)
        self.label.grid(column=0, row=1, sticky="wn",rowspan=1,padx=15,pady=5)
        self.textbox.grid(column=0, row=1,sticky=" news", padx=15,pady=25)
        self.gptversion_label.grid(column=0, row=2, sticky="new", padx=15, pady=5)
        self.gptversion_combobox.grid(column=0, row=2, sticky="sew", padx=15, pady=5)
        self.genbutton.grid(column=0, row=3, sticky="nsew", padx=15, pady=5)
        self.generationout_label.grid(column=0, row=4, sticky="new", padx=15, pady=5)
        self.generation_textbox.grid(column=0, row=4, sticky="snew", padx=15, pady=25)
        
    def generate(self, event=None):
        selected_string = self.instructions_combobox.get()
        selected_numerical_value = self.string_to_number_mapping.get(selected_string)
        
        text = self.textbox.get("1.0", "end-1c")
        generation = self.aigen_instance.generate_response(str(text), selected_numerical_value, self.gptversion.get())
        # clear generation text box
        self.generation_textbox.delete("1.0", tk.END)
        self.generation_textbox.insert(tk.END, generation)
        
        # Get the selected numerical value using the mapping
        print(f"Selected Numerical Value: {selected_numerical_value}")
        
