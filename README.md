# QR Code Generator

A simple GUI application built with Python and Tkinter that allows users to generate QR codes from input data. The generated QR code is saved in the Downloads folder, displayed in the app window, and the folder containing the QR code is opened automatically.

## Features
- User-friendly interface built using Tkinter.
- Generate QR codes based on user input.
- Save generated QR codes as PNG images in the "QRCode_Images" folder located in the Downloads folder.
- Automatically open the folder containing the generated QR codes.
- Clear input and reset the displayed QR code with a single click.

## Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `qrcode` library
- `Pillow` library

## Installation

1. Clone this repository:
- git clone https://github.com/your-username/qr-code-generator.git
- cd qr-code-generator

2. Create and activate a virtual environment (optional, but recommended):
- python -m venv venv
- # On Windows
- venv\Scripts\activate
- # On macOS/Linux
- source venv/bin/activate

3. Install the required dependencies:
- pip install -r requirements.txt

4. Run the application:
- python app.py

## Usage
- Open the application.
- Enter the data (text, URL, etc.) you want to encode into a QR code.
- Click the "Generate QR Code" button.
- The generated QR code will be displayed in the app and saved as a PNG image in the "QRCode_Images" folder inside your Downloads folder.
- The folder will automatically open for easy access to your QR code.
- To clear the input field and reset the QR code display, click the "Clear Input" button. 

## Folder Structure
- app.py: Main Python script for the application.
- requirements.txt: List of required Python libraries.
- README.md: This file.

## Troubleshooting
- Permission Error: If the app fails to create a folder in the Downloads directory, check your system permissions.
- Empty Input Error: Make sure to enter data into the text box before generating the QR code.