import tkinter as tk
from tkinter import ttk
import os
import json

CONFIG_FILE = "audio_settings.json"

# Function to adjust volume and mute settings
def set_volume(master, headphone, speaker, speaker_mute, headphone_mute):
    os.system(f"amixer -q set Master {master}% --")
    if headphone_mute:
        os.system("amixer -q set Headphone 0% mute --")
    else:
        os.system(f"amixer -q set Headphone {headphone}% unmute --")
    if speaker_mute:
        os.system("amixer -q set Speaker 0% mute --")
    else:
        os.system(f"amixer -q set Speaker {speaker}% unmute --")

# Save current settings to a file
def save_defaults():
    settings = {
        "master_volume": master_slider.get(),
        "headphone_volume": headphone_slider.get(),
        "speaker_volume": speaker_slider.get(),
        "speaker_mute": speaker_var.get(),
        "headphone_mute": headphone_var.get(),
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file)
    print("Settings saved!")

# Load settings from file if it exists
def load_defaults():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            settings = json.load(file)
        return settings
    else:
        # Return hardcoded defaults if no saved file exists
        return {
            "master_volume": 92,
            "headphone_volume": 92,
            "speaker_volume": 0,
            "speaker_mute": 0,
            "headphone_mute": 0,
        }

# Callback for sliders and checkboxes
def on_slider_change(*args):
    try:
        master_volume = master_slider.get()
        headphone_volume = headphone_slider.get()
        speaker_volume = speaker_slider.get()
        speaker_mute = speaker_var.get()
        headphone_mute = headphone_var.get()
        set_volume(master_volume, headphone_volume, speaker_volume, speaker_mute, headphone_mute)
    except NameError:
        pass  # Ignore errors during initialization

# Functions for fine-tuning sliders
def adjust_master(value):
    master_slider.set(master_slider.get() + value)

def adjust_headphone(value):
    headphone_slider.set(headphone_slider.get() + value)

def adjust_speaker(value):
    speaker_slider.set(speaker_slider.get() + value)

# Load saved or default settings
default_settings = load_defaults()

# Create the main application window
root = tk.Tk()
root.title("Audio Settings")

# Master Volume
tk.Label(root, text="Master Volume").pack(pady=5)

master_frame = tk.Frame(root)
master_frame.pack(pady=5)
tk.Button(master_frame, text="-", command=lambda: adjust_master(-1)).pack(side=tk.LEFT)
master_slider = ttk.Scale(master_frame, from_=0, to=100, orient="horizontal", command=on_slider_change)
master_slider.set(default_settings["master_volume"])
master_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
tk.Button(master_frame, text="+", command=lambda: adjust_master(1)).pack(side=tk.LEFT)

# Headphone Volume
tk.Label(root, text="Headphone Volume").pack(pady=5)

headphone_frame = tk.Frame(root)
headphone_frame.pack(pady=5)
tk.Button(headphone_frame, text="-", command=lambda: adjust_headphone(-1)).pack(side=tk.LEFT)
headphone_slider = ttk.Scale(headphone_frame, from_=0, to=100, orient="horizontal", command=on_slider_change)
headphone_slider.set(default_settings["headphone_volume"])
headphone_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
tk.Button(headphone_frame, text="+", command=lambda: adjust_headphone(1)).pack(side=tk.LEFT)

# Headphone Mute Checkbox
headphone_var = tk.IntVar(value=default_settings["headphone_mute"])
headphone_checkbox = ttk.Checkbutton(
    root, text="Mute Headphone", variable=headphone_var, onvalue=1, offvalue=0, command=on_slider_change
)
headphone_checkbox.pack(pady=10)

# Speaker Volume
tk.Label(root, text="Speaker Volume").pack(pady=5)

speaker_frame = tk.Frame(root)
speaker_frame.pack(pady=5)
tk.Button(speaker_frame, text="-", command=lambda: adjust_speaker(-1)).pack(side=tk.LEFT)
speaker_slider = ttk.Scale(speaker_frame, from_=0, to=100, orient="horizontal", command=on_slider_change)
speaker_slider.set(default_settings["speaker_volume"])
speaker_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
tk.Button(speaker_frame, text="+", command=lambda: adjust_speaker(1)).pack(side=tk.LEFT)

# Speaker Mute Checkbox
speaker_var = tk.IntVar(value=default_settings["speaker_mute"])
speaker_checkbox = ttk.Checkbutton(
    root, text="Mute Speaker", variable=speaker_var, onvalue=1, offvalue=0, command=on_slider_change
)
speaker_checkbox.pack(pady=10)

# Save Defaults Button
save_button = ttk.Button(root, text="Save Defaults", command=save_defaults)
save_button.pack(pady=20)

# Apply current settings to alsamixer
set_volume(
    master_slider.get(),
    headphone_slider.get(),
    speaker_slider.get(),
    speaker_var.get(),
    headphone_var.get(),
)

# Start the application loop
root.mainloop()
