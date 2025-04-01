import qrcode
import os


def get_next_filename(base_path, base_name, extension):
    """
    Generate the next available filename by incrementing a number.
    """
    counter = 1
    while True:
        # Construct the full file path
        file_path = os.path.join(base_path, f"{base_name}{counter}.{extension}")
        
        # Check if the file path already exists
        if not os.path.exists(file_path):
            return file_path
        counter += 1


base_path = "C:/Users/Martin/OneDrive/Desktop/QRCode/example_outputs"
base_name = "output"
extension = "png"

# Ensure the output folder exists
os.makedirs(base_path, exist_ok=True)

# Get the next available filename
next_file_path = get_next_filename(base_path, base_name, extension)

# Create QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Add data to the QR code (with input validation)
while True:
    data = input("Add data to QR Code: ")
    if data.strip():  # Check if input is not empty
        break
    print("Input cannot be empty. Please try again.")
qr.add_data(data)
qr.make(fit=True)

# Create image from the QRCode instance
img = qr.make_image(fill_color=(255, 195, 235), back_color=(55, 95, 35))
img.save(next_file_path)

print(f"File saved to: {next_file_path}.")
