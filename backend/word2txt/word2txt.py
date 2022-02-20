import docx2txt

def docx2txt(doc_filepath, txt_filepath):

    try:
        text = docx2txt.process(doc_filepath)

        with open(txt_filepath,"w",encoding="UTF-8") as ifile:
            ifile.write(text)
        
        return True

    except Exception as e:
        print(e.message)
        return False


if __name__ == "__main__":
    doc_path = ".\word2pdf\sample.docx"
    txt_save_path = ".\word2txt\sample.txt"

    status = docx2txt(doc_path,txt_save_path)
    
    if (status):
        print("Success")
    else:
        print("Failed")











