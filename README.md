# 📄 PDF to Word Converter

> A powerful, free, and open-source web application for converting PDF files to editable Word documents (.docx)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0%2B-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PDF to Word Converter is a simple yet powerful web application built with **Streamlit**. It allows users to upload PDF files and convert them into editable Word documents (.docx) directly in the browser - **completely free with no file size limits**!

<img src="demo.png"><br/>
<i>Sample </i>

---

## Table of Contents

1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Project Structure](#-project-structure)
4. [Use Cases](#-use-cases)
5. [Tech Stack](#-tech-stack)
6. [Installation](#-installation)
7. [Feature Details](#-feature-details)
8. [How It Works](#-how-it-works)
9. [Known Issues](#-known-issues)
10. [Future Enhancements](#-future-enhancements)
11. [License](#-license)
12. [Contributing](#-contributing)
13. [Contact](#-contact)

---

## 🚀 Project Overview

### 1. This app is designed to:

- Upload PDF files up to **200MB**.
- Convert PDF pages into **.docx Word files**.
- Provide real-time feedback in a user-friendly Streamlit interface.
- Support both **single file conversion** and **multiple files** (zipped).

### 2. Why this project?

- Many existing PDF-to-Word tools are paid or limit free usage.
- This is a lightweight, open-source alternative for **students, office workers, and researchers**.

---

## ✨ Features

| Feature Name               | Description                                          | Library Used              |
| -------------------------- | ---------------------------------------------------- | ------------------------- |
| **Single File Conversion** | Upload and convert a PDF into `.docx`.               | `pdf2docx`, `python-docx` |
| **Batch Conversion**       | Convert multiple PDFs and download as `.zip`.        | `zipfile`, `io.BytesIO`   |
| **Clean UI**               | Simple drag-and-drop interface powered by Streamlit. | `streamlit`               |
| **Safe Filenames**         | Auto-generate filenames with hash + timestamp.       | `hashlib`, `time`         |

---

## 📁 Project Structure

```
├── converter/
│ └── pdf_to_docx.py # Conversion logic
├── utils/
│ └── file_ops.py # File handling utilities (safe names, timestamp, etc.)
├── streamlitApp.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── demo.png demo screenshots
├── LICENSE
└── README.md

```

---

## 🎯 Use Cases

| Use Case             | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **Students**         | Convert lecture notes in PDF into editable Word for annotation. |
| **Office Work**      | Edit reports/contracts that are only available in PDF.          |
| **Batch Processing** | Convert multiple academic papers at once into `.docx`.          |
| **Educational Tool** | Demonstrate PDF parsing & document processing with Python.      |

---

## 🛠️ Tech Stack

| Purpose           | Libraries Used                     |
| ----------------- | ---------------------------------- |
| **PDF Parsing**   | `pdf2docx`                         |
| **Word Creation** | `python-docx`                      |
| **UI/Frontend**   | `streamlit`                        |
| **Helpers**       | `hashlib`, `time`, `io`, `zipfile` |

---

## 📦 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/VuTuanAnh0949/PDF_to_Word_Converter.git
cd PDF_to_Word_Converter
```

### 2. Create virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the app:

```bash
streamlit run streamlitApp.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 💡 Feature Details

### 1. File Upload

- Drag and drop multiple PDF files.
- Each file is validated for size (≤200MB).

### 2. Conversion Logic

For each PDF:

- Parse with `pdf2docx.Converter`.
- Create Word document using `python-docx`.
- Save with **unique name** (`filename-<hash>-<timestamp>.docx`).

### 3. Batch Mode

- If multiple files uploaded, results are zipped automatically.
- Users can download .zip containing all .docx outputs.

---

## ⚙️ How It Works

```bash
Input PDF → pdf2docx → Extract text/images → Write into .docx → Safe filename → Download
```

- **Single file:** Direct `.docx` download.
- **Multiple files:** Auto-zip packaging.

---

## ⚠️ Known Issues

| Issue                | Reason                             | Fix                         |
| -------------------- | ---------------------------------- | --------------------------- |
| **Complex layouts**  | Tables/images may not convert 100% | Manual adjustment in Word   |
| **Large files slow** | Conversion speed depends on #pages | Show progress bar in future |
| **Fonts mismatch**   | PDF fonts may not exist in Word    | Edit styles manually        |

---

## 🚀 Future Enhancements

- Add cloud storage integration (Google Drive/Dropbox).
- Support scanned PDFs → OCR → Word with pytesseract.
- Add progress bar in Streamlit for long files.
- Support DOCX → PDF reverse conversion.

---

## 📜 LICENSE

This project is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/VuTuanAnh0949/pdf-to-word-converter/issues).

### How to contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Vũ Tuấn Anh**

- Email: [vutuananh0949@gmail.com](mailto:vutuananh0949@gmail.com)
- GitHub: [@VuTuanAnh0949](https://github.com/VuTuanAnh0949)

---

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

<div align="center">
  <sub>Built with ❤️ by Vũ Tuấn Anh</sub>
</div>
