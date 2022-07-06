from docx2pdf import convert
import logging

def convert_docx2pdf(src_file_path, dest_file_path):

    logging.info("convert_docx2pdf function execution started.")

    try:
        convert(src_file_path,dest_file_path)
        return True

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

     




