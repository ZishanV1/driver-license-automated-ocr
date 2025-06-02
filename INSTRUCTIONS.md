STEP 1.
Install the required Python libraries by opening your terminal and running:
pip install opencv-python pytesseract openpyxl watchdog pillow

Install Tesseract-OCR:

On Windows: Download from https://github.com/tesseract-ocr/tesseract

On Mac (with Homebrew): brew install tesseract

On Linux (with APT): sudo apt install tesseract-ocr

STEP 2.
Find the full path to the Tesseract executable on your computer.
In your detect_test.py file, add this line at the top:
pytesseract.pytesseract.tesseract_cmd = r'YOUR_PATH_HERE'
For example, on Windows it might be:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

STEP 3.
Create and organize your project folder like this:

watch_and_process.py

detect_test.py

data.xlsx

uploads/ (this folder will store driver's license images)

If the uploads folder doesn't exist, create it:
mkdir uploads

STEP 4.
Add one or more driver's license images (e.g., .jpg or .png) to the uploads/ folder.
Example:
uploads/license1.jpg

STEP 5.
Open your terminal, navigate to the project folder, and run:
python watch_and_process.py
This will start the directory watcher using Watchdog.

STEP 6.
Whenever a new image is added to the uploads folder, the script will:

Detect the image

Extract license details using detect_test.py

Append the extracted data to data.xlsx automatically

STEP 7.
Open data.xlsx to view the results. Each new license added will create a new row with the extracted information.

You’re done. The system now runs hands-free and updates your Excel file in real time whenever new images are uploaded.
