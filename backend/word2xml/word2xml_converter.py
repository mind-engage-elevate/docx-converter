from docx_utils.flatten import opc_to_flat_opc
import logging

def convert_docx2xml(src_file, dest_file):

    logging.info("convert_docx2xml function execution started.")

    try:
        opc_to_flat_opc(src_file, dest_file)
        # opc_to_flat_opc('.\input_files\STUCRA.docx', '.\output_files\abc.xml')
        return True
    
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

if __name__ == "__main__":
    convert_docx2xml('.\input_files\STUCRA.docx', '.\output_files\abc.xml')

