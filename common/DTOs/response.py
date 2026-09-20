class Response:
    def __init__(self,is_succes:bool,message:str,data = None):
        self.succes = is_succes
        self.message = message
        self.data = data