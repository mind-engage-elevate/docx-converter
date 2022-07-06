import docx2txt
import logging 

def convert_docx2txt(doc_filepath, txt_filepath):

    logging.info("convert_docx2txt function execution started.")

    try:
        text = docx2txt.process(doc_filepath)

        with open(txt_filepath,"w",encoding="UTF-8") as ifile:
            ifile.write(text)
        
        return True

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False


    
