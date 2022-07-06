from word2xml.word2xml_converter import convert_docx2xml
from word2txt.word2txt_converter import convert_docx2txt
from word2pdf.word2pdf_converter import convert_docx2pdf
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
import logging , datetime, time 
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.mount("/output_files", StaticFiles(directory="output_files"), name="media") 
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True , allow_methods=["*"], allow_headers=["*"])


SERVER_ADDRESS = "127.0.0.1:8000"

# Setting the required configuration for logging 
def set_logging_config():

    # Creating a new file for log
    global time
    global log_filename
    time = datetime.datetime.now()
    time=time.strftime("%d%m%Y_%H%M%S")
    log_filename = 'app'+ time  +'.log'
    log_file_path = f"app_log_files/{log_filename}"
    # Defining the filename & filemode for log and formate how will it write in log file
    logging.basicConfig(filename= log_file_path, filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    return

# Saving the input file 
def save_input_file(uploaded_file: UploadFile = File(...)):
    logging.info("Saving Your File")
    try:
        global src_file_path
        src_file_path = f"input_files\{uploaded_file.filename}"
        with open(src_file_path , 'wb+') as input_file:
            content=uploaded_file.file.read()
            input_file.write(content)
        logging.info("File has been saved")    
        return True    
    except Exception as e:
        logging.error("Exception occurred", exc_info=True) 
        return False

# Creating the destination path
def create_dest_file(uploaded_file: UploadFile, req_format):
    logging.info("Creating your destination file.")
    file_name = uploaded_file.filename
    global dest_file
    dest_file = file_name.split('.') 
    dest_file = dest_file[0]
    dest_file =  dest_file + time  +'.' + req_format 
    dest_file_path = f"output_files\{dest_file}"
    return dest_file_path



@app.post("/upload-file")
def upload_file(upload_file: UploadFile =File(...), required_format: str=Form(...) ):
    
    set_logging_config() 
   
    valid_document_types = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']

    global status

    # Validating the file format
    if upload_file.content_type in valid_document_types:
        logging.info('File Read Successfully')

        if save_input_file(upload_file):
            required_format = required_format.lower()
            dest_file_path =create_dest_file(upload_file, required_format)

            logging.info(f'Desired format is {required_format}.')

            # Calling the right function to convert the file
            if required_format == 'xml':
                status = convert_docx2xml(src_file_path, dest_file_path)

            elif required_format == 'txt':
                status = convert_docx2txt(src_file_path, dest_file_path)

            elif required_format == 'pdf':
                status = convert_docx2pdf(src_file_path, dest_file_path)
            
            else:
                logging.warning("Required format is not supported.")
                status = False 
                
            # Checking the status whether it is true or not 
            if status :
                logging.info('Finally, File has been converted successfully.')
            else:
                logging.info('Ops!! Found some error, please rectify it.')
        else:
            logging.error("Error saving input File", exc_info=True)      

    else:
        logging.error('Wrong File format has been uploaded.')
        return {"Error detected"}

    if status:    
        # return {"Destination File Path": f"{SERVER_ADDRESS}/output_files/{dest_file}"} 
        return {"Destination File Path": dest_file}; 
    return "Found some error"


   