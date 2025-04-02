import os
import qrcode
from pathlib import Path
import platform
import subprocess


def get_downloads_path():
    """
    Get the Downloads folder path in a cross-platform manner.
    """
    # Use Path.home() to get the user's home directory and append 'Downloads'
    return str(Path.home() / "Downloads")


# Get the correct Downloads folder path using the function
downloads = get_downloads_path()

# Define the name of the folder where QR code images will be saved
folder_name = "QRCode_Images"

# Create the full path for the new folder inside Downloads
folder_path = os.path.join(downloads, folder_name)

# Check if the folder exists; if not, create it
if not os.path.exists(folder_path):  # If the folder doesn't exist
    try:
        os.makedirs(folder_path)  # Create the folder and any intermediate directories
        print(f"Folder '{folder_name}' created successfully in Downloads.")
    except PermissionError:  # Handle permission errors
        print("Permission denied: Unable to create folder in Downloads.")
    except Exception as e:  # Catch other exceptions and print them
        print(f"An error occurred: {e}")
else:
    print(f"Folder '{folder_name}' already exists in Downloads.")  # Inform if folder already exists

def get_next_filename(base_path, base_name, extension):
    """
    Generate the next available filename by incrementing a counter.
    """
    counter = 1
    while True:
        # Construct a filename
        file_path = os.path.join(base_path, f"{base_name}{counter}.{extension}")
        
        # Check if this filename already exists; if not, return it
        if not os.path.exists(file_path):
            return file_path  # Return the first available filename
        counter += 1  # Increment counter to try next number

# Define base name and extension for QR code files
base_name = "qrcode_"  # Base name for QR code files
extension = "png"  # File extension for QR code images

# Get the next available filename in the specified folder
next_file_path = get_next_filename(folder_path, base_name, extension)

# Create an instance of QRCode with specific settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

while True:
    data = input("Add data to QR Code: ")
    if data.strip():  # Ensure input is not empty or just whitespace
        break  # Exit loop if valid input is provided
    print("Input cannot be empty. Please try again.")  # Prompt user again for valid input

qr.add_data(data)  # Add user-provided data to QR code instance
qr.make(fit=True)  # Optimize size of QR code based on input data

# Create an image from the QRCode instance with custom colors
img = qr.make_image(fill_color=(173, 235, 179), back_color=(0, 32, 63))  

# Save the generated QR code image to the next available file path
try:
    img.save(next_file_path)
    print(f"QR Code saved successfully at: {next_file_path}")
    
    # Open the folder containing the QR codes after saving (cross-platform)
    if platform.system() == "Windows":
        os.startfile(folder_path)  # Open folder on Windows using os.startfile()
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", folder_path])  # Use 'open' command to open folder on macOS
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", folder_path])  # Use 'xdg-open' command to open folder on Linux

except Exception as e:  
    print(f"An error occurred while saving the QR Code: {e}")
