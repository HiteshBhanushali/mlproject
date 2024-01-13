import logging
import sys
import logger

def error_messsage_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message  = "Error occurend in python code in file name [{0}] at line no [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail):
        super().__init__(error_message)
        self.error_message = error_messsage_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        
        return self.error_message
    

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Exception in Exception file")
        raise CustomException(e, sys)