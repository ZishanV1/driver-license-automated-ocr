# driver-license-automated-ocr
This project is an automated optical character recognition (OCR) pipeline designed to extract key data from driver's licenses and seamlessly populate it into an Excel spreadsheet—reducing manual data entry by over 45%. The system uses Python and OpenCV for high-accuracy image preprocessing and text extraction, including names, dates of birth, license numbers, and expiration dates across all 50 U.S. states.

To enable real-time automation, the solution integrates Dogwatch, a lightweight directory monitoring library. Once a new image is placed in the designated folder (e.g., scanned or dropped in via cloud sync), Dogwatch automatically triggers the OCR process, parses the license details, and appends the information into an organized Excel sheet. This fully hands-off system drastically improves operational efficiency in client intake processes, especially in fast-paced medical and testing environments.

Must link via google cloud.
