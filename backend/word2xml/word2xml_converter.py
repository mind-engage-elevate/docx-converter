from docx_utils.flatten import opc_to_flat_opc
import logging

def convert_docx2xml(src_file, dest_file):
    """ convert_docx2xml is a method to convert docx file to xml format 
    which take two paramter sourcefile and destinationfile. """

    logging.info("convert_docx2xml function execution started.")

    try:
        opc_to_flat_opc(src_file, dest_file)
        return True
    
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

if __name__ == "__main__":
    convert_docx2xml('.\input_files\sample.docx', '.\output_files\abc.xml') 
    """ Here '.\input_files\sample.docx' is an input which we are interested to convert and 
     '.\output_files\abc.xml' is the output file on which we are going to convert to. """

