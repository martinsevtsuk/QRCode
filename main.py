import tkinter as tk
from tkinter import messagebox
import os
import qrcode
from PIL import Image, ImageTk
from pathlib import Path
import platform
import subprocess


def get_downloads_path():
    """
    Get the Downloads folder path in a cross-platform manner.
    
    Returns:
        str: The path to the Downloads folder.
    """
    return str(Path.home() / "Downloads")


def create_folder(folder_path):
    """
    Create a folder if it does not exist.

    Args:
        folder_path (str): The path of the folder to create.
    """
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except PermissionError:
            messagebox.showerror(
                "Error", "Permission denied: Unable to create folder in Downloads."
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def get_next_filename(base_path, base_name, extension):
    """
    Generate the next available filename by incrementing a counter.

    Args:
        base_path (str): The directory where the file will be saved.
        base_name (str): The base name for the file.
        extension (str): The file extension.

    Returns:
        str: A unique file path for the new file.
    """
    counter = 1
    while True:
        file_path = os.path.join(base_path, f"{base_name}{counter}.{extension}")
        if not os.path.exists(file_path):
            return file_path
        counter += 1


def generate_qr_code():
    """
    Generate a QR code based on user input and save it to the Downloads folder.
    Displays the QR code image in the app and opens the folder containing it.
    """
    # Get user input from the text box
    data = data_entry.get("1.0", tk.END).strip()
    
    if not data:
        messagebox.showerror("Error", "Input cannot be empty!")
        return

    # Define folder for saving QR codes
    downloads_folder = get_downloads_path()
    folder_name = "QRCode_Images"
    folder_path = os.path.join(downloads_folder, folder_name)
    
    # Create the folder if it doesn't exist
    create_folder(folder_path)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Customize QR code colors
    img = qr.make_image(fill_color=(173, 235, 179), back_color=(0, 32, 63))

    # Save QR code image to a unique file path
    next_file_path = get_next_filename(folder_path, "qrcode_", "png")
    
    try:
        img.save(next_file_path)
        
        # Inform user about successful save operation
        messagebox.showinfo(
            "Success", f"QR Code saved successfully at:\n{next_file_path}"
        )

        # Display the QR code image in the app
        qr_image = ImageTk.PhotoImage(Image.open(next_file_path))
        qr_label.config(image=qr_image)
        qr_label.image = qr_image

        # Open the folder containing QR codes (cross-platform)
        if platform.system() == "Windows":
            os.startfile(folder_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", folder_path])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", folder_path])
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the QR Code: {e}")


def clear_input():
    """
    Clear the input text box and reset the displayed QR code image.
    """
    data_entry.delete("1.0", tk.END)
    qr_label.config(image="")
    qr_label.image = None


# Create main Tkinter window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x600")  # Set window size
window.configure(bg="#123458")

# Add title label to the window
title_label = tk.Label(window, text="QR Code Generator", font=("Helvetica", 20), bg="#123458", fg="#F1EFEC", pady=10)
title_label.pack()

# Add label and text box for user input
data_label = tk.Label(window, text="Enter Data:", font=("Helvetica", 16), bg="#123458", fg="#F1EFEC")
data_label.pack()

data_entry = tk.Text(window, height=5, width=40,font=("Helvetica", 16), bg="#D4C9BE")
data_entry.pack(pady=10)

# Add buttons for generating QR code and clearing input
generate_button = tk.Button(
    window,
    text="Generate QR Code",
    command=generate_qr_code,
    bg="#030303",
    fg="#F1EFEC",
    font=("Helvetica", 14),
)
generate_button.pack(pady=10)

clear_button = tk.Button(
    window,
    text="Clear Input",
    command=clear_input,
    bg="#030303",
    fg="#F1EFEC",
    font=("Helvetica", 14),
)
clear_button.pack(pady=10)

# Label to display generated QR code image
qr_label = tk.Label(window, bg="#123458")
qr_label.pack(pady=20)

# Run Tkinter event loop
window.mainloop()
