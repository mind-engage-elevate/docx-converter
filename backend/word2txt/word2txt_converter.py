import docx2txt
import logging 

def convert_docx2txt(doc_filepath, txt_filepath):
    """ convert_docx2txt is a method to convert docx file to text format 
        which take two paramter sourcefile and destinationfile. """

    logging.info("convert_docx2txt function execution started.")

    try:
        text = docx2txt.process(doc_filepath)

        with open(txt_filepath,"w",encoding="UTF-8") as ifile:
            ifile.write(text) # Writing into destination file
        
        return True

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

if __name__ == "__main__":
    convert_docx2txt('.\input_files\sample.docx', '.\output_files\abc.txt') 
    """ Here '.\input_files\sample.docx' is an input which we are interested to convert and 
     '.\output_files\abc.txt' is the output file on which we are going to convert to. """

    
