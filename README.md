# decodelabs_task04
# 🖼️ Image Text Recognition using OCR

A Python-based Optical Character Recognition (OCR) project that extracts text from images using the Tesseract OCR engine. This project demonstrates how to convert printed text in image files into editable digital text with minimal code.

---

## 📌 Overview

This application reads an image file, processes it using Tesseract OCR, and prints the extracted text to the console. It also includes basic error handling to notify users if the specified image file cannot be found.

---

## ✨ Features

* Extract text from image files
* Supports common image formats (JPG, JPEG, PNG, BMP, TIFF)
* Uses the Tesseract OCR engine
* Simple and beginner-friendly implementation
* Handles missing image files gracefully
* Easy to customize for different images

---

## 🛠️ Technologies Used

* Python 3
* Pillow (PIL)
* PyTesseract
* Tesseract OCR

---

## 📁 Project Structure

```text
Image_Recognition_Project/
│
├── image_text_extractor.py
├── img1.jpg
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📋 Prerequisites

Before running the project, make sure you have:

* Python 3.8 or later
* Tesseract OCR installed
* Required Python packages installed

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Image_Recognition_Project.git
cd Image_Recognition_Project
```

### 2. Install the required Python packages

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download and install Tesseract OCR.

After installation, update the following line in the Python script if your installation path is different:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ Usage

1. Copy your image into the project folder.
2. Rename it to:

```text
img1.jpg
```

or update the filename in the script:

```python
image_name = "your_image.jpg"
```

3. Run the program:

```bash
python image_text_extractor.py
```

---

## 📷 Example

### Input

```text
img1.jpg
```

### Output

```text
🔄 Image se text read kiya ja raha hai...

✅ --- Extracted Text Start ---
Hello World
This is an OCR example.
--- Extracted Text End ---

```
## 📸 Screenshots

You can add screenshots of the project here to show how the OCR system works.

### ▶️ Example Input Image

<img width="259" height="331" alt="image" src="https://github.com/user-attachments/assets/98b803da-7e36-4d22-b2f9-e08c0681ae86" />

### 🧾 Extracted Text Output
<img width="267" height="303" alt="image" src="https://github.com/user-attachments/assets/3c1f37ed-23a1-408c-a8ca-e75278f78da1" />


### 💻 Program Running
<img width="944" height="502" alt="image" src="https://github.com/user-attachments/assets/ef1663a9-8bc1-4f1b-ab30-7670ac971759" />


---

## ⚠️ Error Handling

If the image file is not found, the program displays a helpful error message indicating that the specified image does not exist in the project directory.

---

## 🚀 Future Improvements

* Graphical User Interface (GUI)
* Drag-and-drop image upload
* PDF text extraction
* Batch image processing
* Multiple language OCR support
* Export extracted text to TXT or PDF
* Image preprocessing for improved OCR accuracy

---

## 📄 Requirements

Contents of `requirements.txt`

```text
Pillow
pytesseract
```

---

## 👩‍💻 Author

**Zahra Batool**

---

## 📜 License

This project is intended for educational and learning purposes. Feel free to use and modify it for personal or academic projects.
