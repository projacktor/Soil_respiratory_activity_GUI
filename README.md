# Respiratory activity

### Introduction
Respiratory activity is the application for calculating respiratory activity of the soil. The application created for
using in laboratory research. The application allows 4 ways to measure soil's respiratory activity (SRA):
in laboratory conditions via gas chromatograph; in laboratory conditions via titration method; in field conditions via
gas chromatograph; in field conditions via СО₂ analysis. The user can also calculate SRA in Excel-tables 
via additional menu

***
### How to use the application?
Unfortunately, the application supports only Russian language due to the fact that it was created primarily for use in
the Kazan Federal University.

#### Main menu
![main-menu](assets/main_menu_screen.png)
There a user can choose the way of measuring SRA or start working with an Excel-table
pushing the last button.
***
#### Calculating SRA for the single case
![single-case](assets/single-case_calc_menu_screen.png)
First four buttons lead to the four same menus for calculating SRA in different conditions.
The menu contains fields for input values (some of them has already entered values - those are default values, user can
easily change them), radio buttons for choosing the measurements of the output values, window for the output values.
##### Work process:
1) First of all, the user should input values to the following filedes (the fields will not scan the numbers with the comma
, use the point instead).
2) Secondly, choose the measurement of the output value pushing the radio button.
3) Finally, push the output button and see the value
![competed-single-case](assets/single-case_comp_screen.png)
***
#### Working with Excel-tables

<img src="assets/microsoft_office_excel_logo_icon_145720.ico" alt="drawing" width="50">

![excel-working](assets/exel-menu_scree.png)
This menu allows the user load the Excel-table with the SRA input values. The program will return new 
Excel-table with the output values. To receive valid new file, the user should load file using the example introduced on the page.
##### Work process:
1) First of all, the user should load a file. The absolute path to the file will be written in the field above load button 
after the loading.
2) Further, the user should push radio button to choose the measurement of the output values
3) Finally, press the start calculating button to receive new files with the output values. New file will be created in the same directory as the loaded file.
![comp-exel-working](assets/excel-working_compl-screen.png)
***
The application was created using PyQt5 for GUI creating and OpenPyXl for working with Excel. The application was created for
Kazan Federal University researches and has state registration - <a href="https://new.fips.ru/registers-doc-view/fips_servlet?DB=EVM&rn=6295&DocNumber=2023669585&TypeFile=html"> State registratio </a>

![Qt](assets/icons8-qt.svg)
<img src="assets/microsoft_office_excel_logo_icon_145720.ico" alt="drawing" width="50">
