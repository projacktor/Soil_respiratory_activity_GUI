# 🌱 Respiratory Activity

![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

[![PyQt5][PyQt5]][PyQt5-url]
[![OpenPyXL][OpenPyXL]][OpenPyXL-url]
[![Python][Python]][Python-url]

---

### 📘 Introduction

**Respiratory Activity** is a desktop application for calculating the soil’s respiratory activity (SRA). It was developed primarily for laboratory research at **Kazan Federal University**. 🌍

The app supports four different methods of SRA measurement:

- 🧪 In-lab via gas chromatograph  
- ⚗️ In-lab via titration  
- 🌿 In-field via gas chromatograph  
- 🍃 In-field via CO₂ analysis  

Additionally, you can process and calculate SRA directly from **Excel tables** using a dedicated menu. 📊

---

### 🛠 How to Use the Application?

> ⚠️ *Currently, the application is available only in **Russian**, as it was developed for internal use at Kazan Federal University.*

---

### 🏠 Main Menu

![main-menu](assets/main_menu_screen.png)

From here, you can select a method of SRA calculation or use the **Excel-table** mode by clicking the last button. 🧾

---

### 🧮 Single Case Calculation

![single-case](assets/single-case_calc_menu_screen.png)

The first four buttons lead to screens for each measurement method.  
Each screen contains:

- Input fields (some with default values),
- Radio buttons to select units for output,
- Output display window.

#### 🧭 Workflow:

1. Input values into the respective fields (⚠️ Use a **dot** `.` instead of a comma `,` as the decimal separator).
2. Select the desired output units via radio buttons.
3. Click the calculate button to get your result.

📈 Example output:

![competed-single-case](assets/single-case_comp_screen.png)

---

### 📁 Working with Excel Tables

<img src="assets/microsoft_office_excel_logo_icon_145720.ico" alt="Excel Icon" width="40">

![excel-working](assets/exel-menu_scree.png)

This section lets you upload an Excel file containing input values. The app will generate a new Excel file with the calculated outputs.

#### 🧭 Workflow:

1. Load the Excel file. The file path will appear above the button.
2. Select output measurement units.
3. Click the **Calculate** button. A new Excel file with results will be saved in the same directory. ✔️

📂 Example result:

![comp-exel-working](assets/excel-working_compl-screen.png)

---

### ⚙️ Technologies Used

- 🧩 **PyQt5** – for the graphical interface  
- 📄 **OpenPyXL** – for handling Excel files  
- 🏢 Developed for Kazan Federal University

📄 The application has official registration:  
🔗 [State Registration Certificate (№2023669585)](https://new.fips.ru/registers-doc-view/fips_servlet?DB=EVM&rn=6295&DocNumber=2023669585&TypeFile=html)

---

### 📌 Icons and Credits

![Qt](assets/icons8-qt.svg)
<img src="assets/microsoft_office_excel_logo_icon_145720.ico" alt="Excel Icon" width="40">


[PyQt5]: https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white
[PyQt5-url]: https://riverbankcomputing.com/software/pyqt/intro

[OpenPyXL]: https://img.shields.io/badge/OpenPyXL-1D6F42?style=for-the-badge&logo=microsoft-excel&logoColor=white
[OpenPyXL-url]: https://openpyxl.readthedocs.io/en/stable/

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Windows]: https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white
[Windows-url]: https://www.microsoft.com/en-us/windows
