import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_meassage = "Error occured in python script name [{0}] line number [{1}] with error message [{2}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_frame.f_lineno,str(error))
    return error_meassage

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)           ## dont know why this line to be included !!
        self.error_mesage = error_message_detail(error=error_message,error_detail=error_detail)
        print()

    def __str__(self) -> str:
        return self.error_mesage
    
