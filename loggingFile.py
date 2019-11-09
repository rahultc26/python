import logging


logging.basicConfig(filename = "mylog.log",level = logging.ERROR)
try:
    class overLimitException(Exception):
        def __init__(self,msg):
            self.msg = msg
    
    def withdraw(amount):
        if(amount>500):
            raise overLimitException("withdraw amount less than 500\n")
        
    withdraw(400)
    logging.error("withdraw in progress")
except overLimitException:
    print("over over")
    logging.error("overLimitexception")
finally:
    print("display myself")
    