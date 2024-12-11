# <MINIMAL-ALSAMIXER-GUI>

A simple graphical audio settings tool for Linux built with Python and Tkinter. This application allows users to control master, headphone, and speaker volumes with sliders, as well as mute/unmute options.

## Features
- Adjust Master, Headphone, and Speaker volumes.
- Mute/unmute options for Headphone and Speaker.
- Easy-to-use graphical interface.
- Settings persist across sessions with a JSON configuration.

## Requirements
- Linux OS with ALSA sound system.
- Python 3.10 or higher.

## Installation and Usage

### Option 1: Run from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/monurersoy/minimal-alsamixer-gui.git
   cd minimal-alsamixer-gui

2. Install dependencies:
   ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python audio_gui.py

### Option 2: Use Precompiled Binary (Out-of-the-Box)

1. Download the precompiled binary from the "Releases" section.

2. Make the file executable:
    ```bash
    chmod +x audio_gui

3. Run the application:
    ```bash
    ./audio_gui

*This has been tested on Linux Mint 22 Wilma.

## Reason

I built this mainly because my audio card driver issue and have seen people experiencing similar issue. My headphone jack doesn't recognizing devices and act accordingly. Due to that "Headphone" stays muted in alsamixer and Speaker output doesn't stop. So with this simple GUI i/you can easily adjust the necessary settings.

Master Volume - Headphone Volume - Speaer Volume