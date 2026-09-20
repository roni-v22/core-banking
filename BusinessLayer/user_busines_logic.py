from common.DTOs.response import Response

class UserBusinesLogic:
    def Login(self, username, password):
        if len(username) < 3 or len(password) < 5:
            return  Response(False,"invalid strucure Username or password")

        return Response(True,"login success")
