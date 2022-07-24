from docx2pdf import convert
import logging

def convert_docx2pdf(src_file_path, dest_file_path):
    """ convert_docx2pdf is a method to convert docx file to pdf format 
        which take two paramter sourcefile and destinationfile. """

    logging.info("convert_docx2pdf function execution started.")

    try:
        convert(src_file_path,dest_file_path)
        return True

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

if __name__ == "__main__":
    convert_docx2pdf('.\input_files\sample.docx', '.\output_files\abc.pdf') 
    """ Here '.\input_files\sample.docx' is an input which we are interested to convert and 
     '.\output_files\abc.pdf' is the output file on which we are going to convert to. """
     




