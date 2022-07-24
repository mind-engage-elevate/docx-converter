# Docxconverter
A full-stack website application to convert a word document into either pdf, XML, or text format. <br>
Tech stack used : HTML5, CSS3, JavaScript, FastApi, Python, AJAX, jQuery
- It takes a word document and the required format as input
- Convert that file into required format
- Return the converted file with the same name as that of the input
- Releases log messages for every action it start performing.
<br>
This also make use of 3 modules - docx2txt==0.8, docx_util & docx2pdf. 

To run this project follow the following steps:
- Activate virtual environment as "venv/scripts/activate" in windows.
- Install all the requirements as "pip install -r requirements.txt".
- Run the backend after navigating to backend folder as uvicorn main:app --raload or you can directly run from current directory also but make sure to provide correct path.
- Open the index.html in frontend folder in your browser and enjoy using the application.

## Cheers!
