import sys

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):# type: ignore
        super().__init__(error_message)
        self.error_message=self.get_error_message(error_message,error_detail)

    def get_error_message(self,error_message,error_detail:sys):#type:ignore
        
        _,_,error_tb=error_detail.exc_info()

        if error_tb is not None:
            filename=error_tb.tb_frame.f_code.co_filename
            lineno=error_tb.tb_lineno
            return  f"Error occurred in file [{filename}] at line [{lineno}]: {str(error_message)}"
        else:
            return error_message
        
    
    def __str__(self) -> str:
        return self.error_message